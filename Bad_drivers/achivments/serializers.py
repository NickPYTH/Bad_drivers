from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Achivments


class AchivmentSerializer(serializers.ModelSerializer):

    achivment_name = serializers.CharField(required=True)
    achivment_description = serializers.CharField(required=True)

    small_image = serializers.ImageField(required=True)
    big_image = serializers.ImageField(required=True)

    class Meta:
        model = Achivments
        fields = (
            'achivment_name',
            'achivment_description', 
            'small_image',
            'big_image', 
            )
        extra_kwargs = {
            'achivment_name': {'required': True},
            'achivment_description': {'required': True},
            'big_image': {'required': True}
        }

    def validate(self, attrs):
        
        #if attrs['password'] != attrs['password2']:
        #    raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        achivment = Achivments.objects.create(
            achivment_name=validated_data['achivment_name'], 
            achivment_description=validated_data['achivment_description'],
            small_image=validated_data['small_image'],
            big_image=validated_data['big_image'],
        )

        return achivment