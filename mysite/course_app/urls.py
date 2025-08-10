from .views import *
from rest_framework import routers
from django.urls import path, include



router = routers.SimpleRouter()
# router.register(r'?', ?ViewSet, basename='?')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='login'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('assignment/', AssignmentAPIView.as_view(), name='assignment'),
    path('question/', QuestionAPIView.as_view(), name='question'),
    path('answers/', AnswersAPIView.as_view(), name='answers'),
    path('exam/', ExamAPIView.as_view(), name='exam'),
    path('certificate/', CertificateAPIView.as_view(), name='certificate'),
    path('review/', ReviewAPIView.as_view(), name='review'),
]