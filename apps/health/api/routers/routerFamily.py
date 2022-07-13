from rest_framework.routers import DefaultRouter
from apps.health.api.api import FamilyViewSet

router = DefaultRouter()

router.register('', FamilyViewSet, basename="familyExamination")

urlpatterns = router.urls
