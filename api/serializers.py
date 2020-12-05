from rest_framework import serializers
from .models import Achivment, Report


class AchivmentsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    id = serializers.ImageField(read_only=True)
    achivment_name = serializers.CharField(read_only=True)
    achivment_description = serializers.CharField(read_only=True)
    achivment_icon_id = serializers.CharField(read_only=True)

    class Meta:
        model = Achivment
        fields = '__all__'


class CreateReportsSerializer(serializers.ModelSerializer):
    reports = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Report
        fields = '__all__'
