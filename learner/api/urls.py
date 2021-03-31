
from rest_framework import routers
from .api import StudentTableViewSet, TeacherTableViewSet

router = routers.DefaultRouter()
router.register('studenttable', StudentTableViewSet, 'student')
router.register('teachertable', TeacherTableViewSet, 'teacher')

urlpatterns = router.urls
