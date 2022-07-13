from rest_framework.routers import DefaultRouter
from apps.health.api.api import PhysicalViewSet

router = DefaultRouter()

router.register('', PhysicalViewSet, basename="physicalExamination")

urlpatterns = router.urls