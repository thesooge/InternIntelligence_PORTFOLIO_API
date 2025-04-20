from rest_framework import serializers
from .models import Project, Skill, Achievement, Contact

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'description', 'image', 'technologies', 
                 'github_url', 'live_url', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'proficiency', 'icon', 
                 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'title', 'description', 'date', 'image', 'url',
                 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'message', 
                 'created_at', 'is_read']
        read_only_fields = ['created_at', 'is_read'] 