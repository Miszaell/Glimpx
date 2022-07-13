from rest_framework.routers import DefaultRouter
from apps.health.api.api import ClinicalViewSet

router = DefaultRouter()

router.register('', ClinicalViewSet, basename="clinicalExamination")

urlpatterns = router.urls
