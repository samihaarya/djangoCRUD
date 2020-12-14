from rest_framework import viewsets
from . import models, serializers


class AirlinesViewSets(viewsets.ModelViewSet):
    queryset = models.Airlines.objects.all()
    serializer_class = serializers.AirlinesSerializer


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class TerminalViewset(viewsets.ModelViewSet):
    queryset = models.Terminal.objects.all()
    serializer_class = serializers.TerminalSerializer


class AirbusViewset(viewsets.ModelViewSet):
    queryset = models.Airbus.objects.all()
    serializer_class = serializers.AirbusSerializer


class RouteViewset(viewsets.ModelViewSet):
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer


class AirbusScheduleViewset(viewsets.ModelViewSet):
    queryset = models.AirbusSchedule.objects.all()
    serializer_class = serializers.AirbusScheduleSerializer

