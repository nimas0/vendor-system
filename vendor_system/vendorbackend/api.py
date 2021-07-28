from vendorbackend.models import Photographers
from rest_framework import viewsets, permissions
from .serializers import VendorSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Photographers.objects.all()
    permission_classes = [
        permissions.AllowAny
        ]
    serializer_class = VendorSerializer