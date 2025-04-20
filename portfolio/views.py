from django.conf import settings
from django.core.mail import send_mail
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Project, Skill, Achievement, Contact
from .serializers import ProjectSerializer, SkillSerializer, AchievementSerializer, ContactSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    @action(detail=False, methods=['get'])
    def categories(self, request):
        categories = dict(Skill.CATEGORY_CHOICES)
        return Response(categories)

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAdminOrReadOnly]

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Send email notification
        if hasattr(settings, 'EMAIL_HOST_USER'):
            subject = f"New Contact Form Submission: {serializer.data['subject']}"
            message = f"""
            Name: {serializer.data['name']}
            Email: {serializer.data['email']}
            Subject: {serializer.data['subject']}
            
            Message:
            {serializer.data['message']}
            """
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Failed to send email notification: {e}")
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Your message has been sent successfully!"},
            status=status.HTTP_201_CREATED,
            headers=headers
        ) 