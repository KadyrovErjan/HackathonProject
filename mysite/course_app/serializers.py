from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.get('email')
        user = User(username=email, **validated_data)
        user.set_password(password)
        user.save()
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)

        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "Пользователь с таким email не найден"})

        if not user.check_password(password):
            raise serializers.ValidationError({"password": "Неверный пароль"})

        if not user.is_active:
            raise serializers.ValidationError("Пользователь не активен")

        self.context['user'] = user
        return data

    def to_representation(self, instance):
        user = self.context['user']
        refresh = RefreshToken.for_user(user)

        return {
            'user': {
                'username': user.username,
                'email': user.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get('refresh')
        try:
            RefreshToken(token)
        except Exception:
            raise serializers.ValidationError({"refresh": "Невалидный токен"})
        return attrs


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'full_name', 'email']

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CourseListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    class Meta:
        model = Course
        fields = ['id', 'category_name', 'category', 'price_type',]




class CourseSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name']





class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    created_by = UserProfileListSerializer()
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'category', 'level', 'price_type', 'price', 'video',
                  'created_by', 'created_at', 'updated_at']


class LessonListSerializer(serializers.ModelSerializer):
    course = CourseSimpleSerializer()
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_url', 'course']

class LessonSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title']

class LessonDetailSerializer(serializers.ModelSerializer):
    course = CourseSimpleSerializer()
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_url', 'content', 'course']


class AssignmentSerializer(serializers.ModelSerializer):
    lesson = LessonSimpleSerializer
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'level', 'due_date', 'lesson', 'type',
                  'is_active']

class AssignmentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title']


class QuestionSerializer(serializers.ModelSerializer):
    assignment = AssignmentSimpleSerializer
    class Meta:
        model = Question
        fields = ['id', 'assignment', 'text', 'name_question']


class QuestionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'name_question']


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['id', 'questions', 'answers', 'true_answers']



class ExamSerializer(serializers.ModelSerializer):
    course = CourseSimpleSerializer()
    questions = QuestionSimpleSerializer()
    class Meta:
        model = Exam
        fields = ['id', 'title', 'course', 'questions', 'passing_score', 'is_active']



class CertificateSerializer(serializers.ModelSerializer):
    course = CourseSimpleSerializer()
    student = UserProfileListSerializer()
    class Meta:
        model = Certificate
        fields = ['id', 'student', 'course', 'issued_at', 'certificate_url']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileListSerializer()
    course = CourseSimpleSerializer()
    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'rating', ]


