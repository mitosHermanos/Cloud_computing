# Generated by Django 2.2 on 2021-11-26 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_enrolment', models.DateTimeField(default=django.utils.timezone.now)),
                ('scholarship', models.BooleanField(default=False)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
