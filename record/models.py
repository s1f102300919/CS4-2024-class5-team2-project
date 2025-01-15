from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class StudyRecord(models.Model):
    subject = models.CharField(max_length=100)
    comment = models.TextField()
    elapsed_time = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.elapsed_time}"
