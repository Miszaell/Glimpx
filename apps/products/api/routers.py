from rest_framework.routers import DefaultRouter

from apps.products.api.api import MaterialViewSet

router = DefaultRouter()

router.register('', MaterialViewSet, basename="materials")

urlpatterns = router.urls
