# chatapp/models.py
from django.db import models

class Chat(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.question} - {self.answer}"
