from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.content
