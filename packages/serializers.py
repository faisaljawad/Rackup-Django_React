from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from packages.models import Package


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

    def validate(self, attrs):
        Count = Package.objects.filter(bids_count=attrs.get('bids_count'))
        if Count < 0:
            raise ValidationError('Please provide a Valid Value')
        return attrs

    def create(self, validated_data):
        pkg = Package.objects.create(**validated_data)
        return pkg

    def update(self, instance, validated_data):
        for param, value in validated_data.items():
            setattr(instance, param, value)
        instance.save()
        return instance
