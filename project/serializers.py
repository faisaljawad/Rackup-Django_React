from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from project.models import Project, Proposal


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def validate(self, attrs):
        skills = Project.objects.filter(skills_required=attrs.get('skills_required')).count()
        if skills < 0:
            raise ValidationError('At least 1 skill should be provided')
        return attrs

    def create(self, validated_data):
        skill = validated_data.pop('skills')

        project = Project.objects.create(**validated_data)
        project.skills.set(skill)

        return project

    def update(self, instance, validated_data):
        skill = validated_data.pop('skills', [])

        for param, value in validated_data.items():
            setattr(instance, param, value)
        instance.save()

        for s in skill:
            instance.courses.add(s)

        return instance


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'

    def validate(self, attrs):
        cover = Proposal.objects.filter(cover_letter=attrs.get('cover_letter'))
        if len(cover) < 0:
            raise ValidationError('A cover Letter is needed to make a Proposal')
        return attrs

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        return project

    def update(self, instance, validated_data):
        for param, value in validated_data.items():
            setattr(instance, param, value)
        instance.save()
        return instance

