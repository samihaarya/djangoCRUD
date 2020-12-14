# converting python data to json for API and vice versa

from rest_framework import serializers
from airlineServiceAPI import models


class AirlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Airlines
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Terminal
        fields = '__all__'


class AirbusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Airbus
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = '__all__'


class AirbusScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AirbusSchedule
        fields = '__all__'

