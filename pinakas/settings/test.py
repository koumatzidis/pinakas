from pinakas.settings.prod import *  # noqa:F401,F403


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'pinakas.sqlite3',
        'DEBUG_NAME': 'pinakas-debug.sqlite3',
    },
}
