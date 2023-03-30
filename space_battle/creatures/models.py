from django.db import models


class SpaceMan(models.Model):
    name = models.CharField(max_length=50)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name


