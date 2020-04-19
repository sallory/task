from django.db import models

# Create your models here.

class Match(models.Model):
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=32)
    human_id = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name