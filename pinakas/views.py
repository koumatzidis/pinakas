import datetime
from django.shortcuts import render
from .models import (
    Announcement, Configuration, Media, Planning, Room, Time,
    SchoolProgramme, Day, DutyTime, DutyLocation, DutyAssignment
)

ENGLISH_TO_GREEK_DAYS = {
    'Monday': 'Δευτέρα',
    'Tuesday': 'Τρίτη',
    'Wednesday': 'Τετάρτη',
    'Thursday': 'Πέμπτη',
    'Friday': 'Παρασκευή',
    'Saturday': 'Σάββατο',
    'Sunday': 'Κυριακή',
}

def get_current_day_object():
    today_name_en = datetime.date.today().strftime('%A')
    today_name_gr = ENGLISH_TO_GREEK_DAYS.get(today_name_en)
    try:
        return Day.objects.get(name__iexact=today_name_gr)
    except Day.DoesNotExist:
        return None

def get_school_programme_grid(current_day):
    grid = {}
    times = Time.objects.all()
    for time in times:
        grid[time.id] = []

    for entry in SchoolProgramme.objects.filter(day=current_day):
        if entry.teacher:
            grid[entry.time.id].append({
                'room': entry.room.name,
                'teacher': entry.teacher.name
            })
    return grid

def get_planning_grid():
    grid = {}
    times = Time.objects.all()
    for time in times:
        grid[time.id] = []

    for entry in Planning.objects.all():
        if entry.teacher:
            grid[entry.time.id].append({
                'room': entry.room.name,
                'teacher': entry.teacher.name
            })
    return grid

def index(request):
    config = Configuration.get_solo()
    context = {}

    emergency_mode = config.emergency_mode
    if emergency_mode:
        screen_mode = 'emergency'
        screen_modes = ['emergency']
        mobile_screen_modes = ['emergency']
        context.update({
            'emergency_title': config.emergency_title,
            'emergency_subtitle': config.emergency_subtitle,
        })
    else:
        screen_mode = request.GET.get('screen_mode', 'informations')
        screen_modes = ['informations', 'SchoolProgramme']
        mobile_screen_modes = ['informations']

        if config.valentine_day and datetime.date.today() == config.valentine_date:
            screen_modes.append('valentine')
        if config.carnival_day and datetime.date.today() == config.carnival_date:
            screen_modes.append('carnival')

    # Ημέρα και grids
    current_day = get_current_day_object()
    school_grid = get_school_programme_grid(current_day) if current_day else {}
    planning_grid = get_planning_grid()

    planning_rooms = Room.objects.filter(planning__teacher__isnull=False).distinct()
    programme_rooms = Room.objects.filter(schoolprogramme__teacher__isnull=False).distinct()

    # Duty grids
    duty_amendments = DutyAssignment.objects.filter(type='amendment')
    duty_times = DutyTime.objects.filter(is_for_duty=True)
    duty_locations = DutyLocation.objects.all()
    today_name = datetime.date.today().strftime('%A')
    try:
        current_day = Day.objects.get(name__iexact=ENGLISH_TO_GREEK_DAYS[today_name])
        duty_daily = DutyAssignment.objects.filter(type='daily', day=current_day)
    except Day.DoesNotExist:
        duty_daily = DutyAssignment.objects.none()

    context.update({
        'enterprise_name': config.enterprise_name,
        'planning': Planning.objects.all(),
        'planning_grid': planning_grid,
        'planning_rooms': planning_rooms,
        'programme_rooms': programme_rooms,
        'announcements': Announcement.objects.all(),
        'times': Time.objects.all(),
        'medias': Media.objects.all(),
        'mobile_screen_modes': mobile_screen_modes,
        'screen_modes': screen_modes,
        'screen_mode': screen_mode,
        'SchoolProgramme': SchoolProgramme.objects.all().order_by('day'),
        'grid': school_grid,
        'day': current_day,
        'duty_amendments': duty_amendments,
        'duty_daily': duty_daily,
        'locations': duty_locations,
        'duty_times': duty_times,
    })

    return render(request, 'index.html', context)