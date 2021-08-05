from rest_framework import serializers
from .models import Photographer
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


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
       # Token.objects.create(user=user)
        return user



    """
    vendor_id = serializers.IntegerField()
    company_name = serializers.CharField(max_length=100)
    # max length of 1000 is randomly picked to handle dictionary length
    address = serializers.CharField(max_length=1000)
    phone_number = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=254)
    availability = serializers.CharField(max_length=1000)

    acceptance_score = serializers.IntegerField()
    total_job_offers = serializers.IntegerField()

    rating_score = serializers.IntegerField()
    total_ratings = serializers.IntegerField()

    fixed_cost = serializers.IntegerField()
    distance_cost = serializers.CharField(max_length=1000)
    size_cost = serializers.CharField(max_length=1000)

    appointments = serializers.CharField()

    def create(self, validated_data):
        return Photographer.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.vendor_id = validated_data.get('vendor_id', instance.vendor_id)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number= validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.availability = validated_data.get('availability', instance.availability)
        instance.acceptance_score = validated_data.get('acceptance_score', instance.acceptance_score)
        instance.total_job_offers = validated_data.get('total_job_offers', instance.total_job_offers)
        instance.rating_score = validated_data.get('rating_score', instance.rating_score)
        instance.total_ratings= validated_data.get('total_ratings', instance.total_ratings)
        instance.fixed_cost= validated_data.get('fixed_cost', instance.fixed_cost)
        instance.distance_cost = validated_data.get('distance_cost', instance.distance_cost)
        instance.size_cost = validated_data.get('size_cost', instance.size_cost)
        instance.appointments = validated_data.get('appointments', instance.appointments)
    """