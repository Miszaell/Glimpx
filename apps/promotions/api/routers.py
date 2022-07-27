from rest_framework.routers import DefaultRouter

from apps.promotions.api.api import PromotionViewSet

router = DefaultRouter()

router.register('', PromotionViewSet, basename="promotions")

urlpatterns = router.urls