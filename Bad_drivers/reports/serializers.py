from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Report, Car



class ReportSerializer(serializers.ModelSerializer):

    car_number = serializers.CharField(required=True)
    car_region = serializers.CharField(required=True)
    car_country = serializers.CharField(required=True)
    data = serializers.DateTimeField(required=True)
    status = serializers.BooleanField(required=True)
    description = serializers.CharField(required=False, default="None")

    image_1 = serializers.ImageField(required=True)
    image_2 = serializers.ImageField(required=True)
    image_3 = serializers.ImageField(required=True)

    class Meta:
        model = Report
        fields = (
            'user_name',
            'car_number', 
            'car_region',
            'car_country', 
            'data', 
            'status', 
            'description', 
            'image_1', 
            'image_2', 
            'image_3'
            )
        extra_kwargs = {
            'car_number': {'required': True},
            'car_region': {'required': True},
            'car_country': {'required': True}
        }

    def validate(self, attrs):
        print("ffffffffffffffffffffffffffffffffffffffff123213")
        #if attrs['password'] != attrs['password2']:
        #    raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        car = Car.objects.create(
                        car_number=validated_data['car_number'],
                        car_region=validated_data['car_region'],
                        car_country=validated_data['car_country']
                            )

        car.save()
        
        report = Report.objects.create(
            user_name=User.objects.get(username=validated_data['user_name']),
            car_number=validated_data['car_number'],
            car_region=validated_data['car_region'],
            car_country=validated_data['car_country'],
            data=validated_data['data'],
            status=validated_data['status'],
            description=validated_data['description'],
            image_1=validated_data['image_1'],
            image_2=validated_data['image_2'],
            image_3=validated_data['image_3']
        )

        report.save()

        return report