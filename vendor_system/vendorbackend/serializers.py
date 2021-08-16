from rest_framework import serializers
from .models import Photographer
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

# Photographer serializer which reads the MySQL data and outputs to readable as JSON 
class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographer
        fields = [
           # 'vendor_id',
            'id',
            'company_name',
            'address',
            'phone_number',
            'email',
            'availability',
            'acceptance_score',
            'total_job_offers',
            'rating_score',
            'total_ratings',
            'fixed_cost',
            'distance_cost',
            'size_cost',
            'appointments',
            'status']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
    
        extra_kwargs = { 'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # Creates a token for each created user
        Token.objects.create(user=user)
        return user


