from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(default='description')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=date.today, editable=False)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.content


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    content_image = models.ImageField(upload_to='answer_images/', blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.content


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "User profiles"

    def __str__(self):
        return self.user.username


class LikeQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "like quizzes"

