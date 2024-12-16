from django.db import models

class Robot(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    intelligence = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.last_name}"
