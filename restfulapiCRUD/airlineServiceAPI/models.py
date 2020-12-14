from enum import Enum

from django.db import models


# Create your models here.


class Airlines(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Employee(models.Model):
    GENDER = (
        ('M', 'MALE'),
        ('F', 'FEMALE')
    )
    JOB = (
        ('hostess', 'HOSTESS'),
        ('pilot', 'PILOT')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    job = models.CharField(max_length=7, choices=JOB, default='pilot')
    airline = models.ForeignKey(Airlines, on_delete=models.CASCADE)

#
# class CabinCrew(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_pilot = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     second_pilot = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     head_host = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     first_host = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     second_host = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     third_host = models.ForeignKey(Employee, on_delete=models.CASCADE)
#


class Terminal(models.Model):
    CITY = (
        ('DEL', 'DELHI'),
        ('MUB', 'MUMBAI'),
        ('PUN', 'PUNE'),
        ('BGL', 'BANGLORE'),
        ('CHD', 'CHANDIGARH'),
        ('AHD', 'AHEMDABAD')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=4)
    city = models.CharField(max_length=3, choices=CITY, default='DEL')


class Airbus(models.Model):
    id = models.AutoField(primary_key=True)
    # cabin_crew = models.ForeignKey(CabinCrew, on_delete=models.CASCADE)


class Route(models.Model):
    CITY = (
        ('DEL', 'DELHI'),
        ('MUB', 'MUMBAI'),
        ('PUN', 'PUNE'),
        ('BGL', 'BANGLORE'),
        ('CHD', 'CHANDIGARH'),
        ('AHD', 'AHEMDABAD')
    )
    id = models.AutoField(primary_key=True)
    from_city = models.CharField(max_length=3, choices=CITY, default='DEL')
    to_city = models.CharField(max_length=3, choices=CITY, default='BGL')
    airbus = models.ManyToManyField(Airbus)


class AirbusSchedule(models.Model):
    STATUS = (
        ('on', 'ON_TIME'),
        ('delayed', 'DELAYED'),
        ('early', 'BEFORE_TIME')
    )
    schedule_id = models.AutoField(primary_key=True)
    airbus = models.ForeignKey(Airbus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    date = models.DateField()
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS, default='on')
    delayed_by = models.IntegerField()
