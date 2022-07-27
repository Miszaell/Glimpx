from rest_framework.routers import DefaultRouter
from apps.health.api.api import AnamnesisViewSet

router = DefaultRouter()

router.register('', AnamnesisViewSet, basename="anamnesis")

urlpatterns = router.urls
