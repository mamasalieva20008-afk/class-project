from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, DirectionViewSet, GroupViewSet

router = DefaultRouter()
router.register('faculties', FacultyViewSet)
router.register('directions', DirectionViewSet)
router.register('groups', GroupViewSet)

urlpatterns = router.urls