# Generated by Django 4.2.18 on 2025-05-15 13:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
import pinakas.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(max_length=20, unique=True, verbose_name="type"),
                ),
                ("message", models.TextField(verbose_name="message")),
            ],
            options={
                "verbose_name": "Ανακοινώσει",
                "ordering": ["type"],
            },
        ),
        migrations.CreateModel(
            name="Configuration",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "enterprise_name",
                    models.CharField(max_length=50, verbose_name="enterprise name"),
                ),
                (
                    "emergency_mode",
                    models.BooleanField(default=False, verbose_name="emergency mode"),
                ),
                (
                    "emergency_title",
                    models.CharField(max_length=50, verbose_name="emergency title"),
                ),
                (
                    "emergency_subtitle",
                    models.CharField(max_length=50, verbose_name="emergency subtitle"),
                ),
                (
                    "carnival_day",
                    models.BooleanField(default=False, verbose_name="carnival day"),
                ),
                (
                    "carnival_date",
                    models.DateField(
                        default=datetime.date(2025, 2, 21), verbose_name="carnival date"
                    ),
                ),
                (
                    "valentine_day",
                    models.BooleanField(default=False, verbose_name="valentine day"),
                ),
                (
                    "valentine_date",
                    models.DateField(
                        default=datetime.date(2023, 2, 14),
                        verbose_name="valentine date",
                    ),
                ),
            ],
            options={
                "verbose_name": "parameters",
            },
        ),
        migrations.CreateModel(
            name="Day",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=15, verbose_name="day")),
            ],
            options={
                "verbose_name": "Ημέρε",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="DutyLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="DutyTime",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "is_for_duty",
                    models.BooleanField(default=True, verbose_name="Πίνακας εφημεριών"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="name")),
                (
                    "image",
                    models.ImageField(
                        upload_to=pinakas.models.format_filename, verbose_name="image"
                    ),
                ),
            ],
            options={
                "verbose_name": "media",
            },
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=15, verbose_name="room")),
            ],
            options={
                "verbose_name": "Αίθουσε",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="teacher")),
            ],
            options={
                "verbose_name": "Καθηγητέ",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Time",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=15, verbose_name="time")),
                ("rank", models.IntegerField(verbose_name="display order")),
            ],
            options={
                "verbose_name": "Ώρες",
                "ordering": ["rank"],
            },
        ),
        migrations.CreateModel(
            name="Planning",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pinakas.room",
                        verbose_name="room",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pinakas.teacher",
                        verbose_name="teacher",
                    ),
                ),
                (
                    "time",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pinakas.time",
                        verbose_name="time",
                    ),
                ),
            ],
            options={
                "verbose_name": "planning",
            },
        ),
        migrations.CreateModel(
            name="SchoolProgramme",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pinakas.day"
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pinakas.room"
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pinakas.teacher",
                    ),
                ),
                (
                    "time",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pinakas.time"
                    ),
                ),
            ],
            options={
                "unique_together": {("day", "room", "time")},
            },
        ),
        migrations.CreateModel(
            name="DutyAssignment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("daily", "Καθημερινή Εφημερία"),
                            ("amendment", "Τροποποιημένη Εφημερία"),
                        ],
                        default="daily",
                        max_length=20,
                        verbose_name="Τύπος",
                    ),
                ),
                (
                    "day",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pinakas.day",
                        verbose_name="Ημέρα",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pinakas.dutylocation",
                        verbose_name="Χώρος",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pinakas.teacher",
                        verbose_name="Καθηγητής",
                    ),
                ),
                (
                    "time",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pinakas.dutytime",
                        verbose_name="Ώρα Εφημερίας",
                    ),
                ),
            ],
            options={
                "verbose_name": "Εφημερία",
                "verbose_name_plural": "Εφημερίες",
                "unique_together": {("type", "day", "time", "location")},
            },
        ),
    ]
