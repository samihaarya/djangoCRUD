from airlineServiceAPI import viewsets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('airlines', viewsets.AirlinesViewSets)
router.register('employee', viewsets.EmployeeViewset)

router.register('terminal', viewsets.TerminalViewset)
router.register('airbus', viewsets.AirbusViewset)

router.register('route', viewsets.RouteViewset)
router.register('schedule', viewsets.AirbusScheduleViewset)
