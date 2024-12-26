from django.db import models
from Santa_list.models import Kid

class Toy(models.Model):
    kid = models.OneToOneField(Kid, on_delete=models.CASCADE)
    toy_type = models.CharField(max_length=100)

    def __str__(self):
        return f"Toy for {self.kid.name}"

class Coal(models.Model):
    kid = models.OneToOneField(Kid, on_delete=models.CASCADE)
    punishment = models.CharField(max_length=100, default="Coal for bad behavior")

    def __str__(self):
        return f"Coal for {self.kid.name}"

