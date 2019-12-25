from curses.ascii import isalpha

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import CustomUser, Certification, Skill, Review, Account, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate(self, attrs):
        fname = CustomUser.objects.filter(first_name=attrs.get('first_name'))
        lname = CustomUser.objects.filter(last_name=attrs.get('last_name'))
        if not isalpha(fname) and not isalpha(lname):
            raise ValidationError('Name Fields can not have digits')
        return attrs

    def create(self, validated_data):
        User = CustomUser.objects.create(**validated_data)
        return User

    def update(self, instance, validated_data):
        for param, value in validated_data.items():
            setattr(instance, param, value)
        instance.save()
        return instance


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

    def validate(self, attrs):
        Count = Certification.objects.filter(name=attrs.get('name')).count()
        if Count > 0:
            raise ValidationError('Certification Already Exists')
        return attrs

    def create(self, validated_data):
        Certificate = Certification.objects.create(**validated_data)
        return Certificate

    def update(self, instance, validated_data):
        for param, value in validated_data.items():
            setattr(instance, param, value)
        instance.save()
        return instance


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

    def validate(self, attrs):
        Count = Skill.objects.filter(name=attrs.get('name')).count()
        if Count > 0:
            raise ValidationError('Skill Already Exists')
        return attrs

    def create(self, validated_data):
        skills = Skill.objects.create(**validated_data)
        return skills

    def update(self, instance, validated_data):
        for param, value in validated_data.items():
            setattr(instance, param, value)
        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, attrs):
        Count = Review.objects.filter(rating=attrs.get('rating'))
        if Count > 5:
            raise ValidationError('Rating Can not EXCEED 5')
        return attrs

    def create(self, validated_data):
        reviews = Review.objects.create(**validated_data)
        return reviews

    def update(self, instance, validated_data):
        for param, value in validated_data.items():
            setattr(instance, param, value)
        instance.save()
        return instance


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate(self, attrs):
        amount = Account.objects.filter(balance=attrs.get('balance'))
        if amount > 300000:
            raise ValidationError('Balance can not EXCEED 300,000')
        return attrs

    def create(self, validated_data):
        account = Account.objects.create(**validated_data)
        return account

    def update(self, instance, validated_data):
        for param, value in validated_data.items():
            setattr(instance, param, value)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def validate(self, attrs):
        rate = Profile.objects.filter(hourly_rate=attrs.get('hourly_rate'))
        if rate < 5:
            raise ValidationError('Rate Can not be less than $5')
        return attrs

    def create(self, validated_data):
        skill = validated_data.pop('skills')
        certification = validated_data.pop('certifications')

        profile = Profile.objects.create(**validated_data)
        profile.skills.set(skill)
        profile.certifications.set(certification)

        return profile

    def update(self, instance, validated_data):
        skill = validated_data.pop('skills', [])
        certification = validated_data.pop('certifications', [])

        for param, value in validated_data.items():
            setattr(instance, param, value)
        instance.save()

        for s in skill:
            instance.courses.add(s)

        for c in certification:
            instance.courses.add(c)

        return instance

