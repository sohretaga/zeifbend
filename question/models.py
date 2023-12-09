from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField()
    true_answer = models.CharField(max_length=1000)
    false_answer = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.true_answer