from rest_framework import serializers
from vendorbackend.models import Photographers

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographers
        fields = '__all__'