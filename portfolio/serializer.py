from rest_framework import serializers
from .models import ContactMessage, Project, Skill, Achievment

class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='project-detail', read_only=True)


    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'link')
        read_only_fields = ('id',)


class SkillSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='skill-detail', read_only=True)


    class Meta:
        model = Skill
        fields = ('id', 'name')
        read_only_fields = ('id',)


class AchievmentSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='achievment-detail', read_only=True)


    class Meta:
        model = Achievment
        fields = ('id', 'title', 'description')
        read_only_fields = ('id',)

class ContactMessageSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='contactmessage-detail', read_only=True)


    class Meta:
        model = ContactMessage
        fields = ('id', 'name', 'subject', 'email', 'message')
        read_only_fields = ('id',)