from django.db import models

class Topic(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.question} - {self.answer}"

class Blog(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000, unique=True)
    content = models.CharField(max_length=1000)
    date = models.IntegerField()

    def __str__(self):
        return f"{self.topic.question} - {self.title} - {self.content} - {self.date}"
