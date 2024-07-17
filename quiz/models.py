from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text
