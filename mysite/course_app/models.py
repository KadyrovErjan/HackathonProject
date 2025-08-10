from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import PositiveSmallIntegerField

ROLE_CHOICES = (
    ('teacher', 'teacher'),
    ('student', 'student')
)

class UserProfile(AbstractUser):
    role = models.CharField(max_length=23, choices=ROLE_CHOICES, default='student')
    full_name = models.CharField(max_length=32, unique=True)

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

class Course(models.Model):
    course_name = models.CharField(max_length=40, unique=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level_choices = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый')
    )
    level = models.CharField(max_length=30, choices=level_choices, default='начальный')
    price_choices = (
        ('Бесплатный', 'Бесплатный'),
        ('Платный', 'Платный')
    )
    price_type = models.CharField(max_length=32, choices=price_choices, default='Бесплатный')
    price = models.PositiveSmallIntegerField()
    video = models.URLField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default='teacher')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Lesson(models.Model):
    title = models.CharField(max_length=32)
    video_url = models.URLField()
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Assignment(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField
    level_assignment_choices = (
        ('лёгкий', 'лёгкий'),
        ('средний', 'средний'),
        ('сложный', 'сложный')
    )
    level: models.CharField(max_length=32, choices=level_assignment_choices, default='лёгкий')
    due_date: models.TimeField
    lesson: models.ForeignKey(Lesson, on_delete=models.CASCADE)
    type_choices = (
        ('текст', 'текст'),
        ('тест', 'тест'),
        ('файл', 'файл'),
    )
    is_active = models.BooleanField(default=False)

class Question(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    text = models.TextField()
    name_question = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name_question}'

class Answers(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.CharField(max_length=64)
    true_answers = models.BooleanField(default=False)

class Exam(models.Model):
    title: models.CharField(max_length=32)
    course: models.ForeignKey(Course, on_delete=models.CASCADE)
    questions: models.TextField()
    passing_score: PositiveSmallIntegerField()
    is_active= models.BooleanField(default=True)

class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.URLField()

    def __str__(self):
        return f'{self.student.username} - {self.course.title}'

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}'