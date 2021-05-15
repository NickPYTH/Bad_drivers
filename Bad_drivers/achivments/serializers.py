from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Achivment, UserAchivment
from minio import Minio
from io import BytesIO


class AchivmentSerializer(serializers.ModelSerializer):

    achivment_name = serializers.CharField(required=True)
    achivment_description = serializers.CharField(required=True)
    small_image = serializers.ImageField(required=True)
    big_image = serializers.ImageField(required=True)

    class Meta:
        model = Achivment
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
        return attrs

    def create(self, validated_data):
        import tempfile

        client = Minio("188.225.83.42:9000", "minioadmin", "minioadmin", secure=False)
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        tmp_file.write(validated_data['big_image'].read())
        big_image = client.fput_object(
            "baddrivers", str(validated_data['achivment_name']) + "_big.jpg", tmp_file.name
        )
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        tmp_file.write(validated_data['small_image'].read())
        small_image = client.fput_object(
            "baddrivers", str(validated_data['achivment_name']) + "_small.jpg", tmp_file.name
        )

        achivment = Achivment.objects.create(
            achivment_name=validated_data['achivment_name'], 
            achivment_description=validated_data['achivment_description'],
            small_image=str(validated_data['achivment_name']) + "_small.jpg",
            big_image=str(validated_data['achivment_name']) + "_big.jpg",
        )



        return achivment

class UserAchivmentSerializer(serializers.ModelSerializer):

    user = serializers.CharField(required=True)
    achivment = serializers.CharField(required=True)
    date = serializers.DateField()

    class Meta:
        model = UserAchivment
        fields = (
            'user',
            'achivment',
            'date',
        )

    def create(self, validated_data):
        user_achivment = UserAchivment.objects.create(
            user=User.objects.get(username=validated_data['user']),
            achivment=Achivment.objects.get(achivment_name=validated_data['achivment']),
            date=validated_data['date']
        )

        return user_achivment