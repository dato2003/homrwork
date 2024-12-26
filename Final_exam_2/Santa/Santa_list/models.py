from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Kid model to store information about the child
class Kid(models.Model):
    name = models.CharField(max_length=255)  # Name of the child
    niceness_coefficient = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])  # Coefficient indicating how nice the child is
    gift = models.CharField(max_length=255)  # Gift the child asks for

    def __str__(self):
        return self.name



class SantaList(models.Model):
    kids = models.ForeignKey(Kid, related_name='santa_lists', on_delete=models.CASCADE,null=True)
    naughty_list = models.ManyToManyField(Kid, related_name='naughty_lists', blank=True,null=True)
    nice_list = models.ManyToManyField(Kid, related_name='nice_lists', blank=True,null = True)

    def create_santas_list(self):

        all_kids = Kid.objects.all()
        for kid in all_kids:
            if kid.niceness_coefficient >= 5:
                self.nice_list.add(kid)
            else:
                self.naughty_list.add(kid)
        self.save()

    def __str__(self):
        return f"Santa's list {self.id}"

