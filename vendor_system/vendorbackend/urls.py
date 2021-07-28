from rest_framework import routers
from .api import VendorViewSet

router = routers.DefaultRouter()
router.register('api/vendor',VendorViewSet,'vendorbackend')

urlpatterns = router.urls