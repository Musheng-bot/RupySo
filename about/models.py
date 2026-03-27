from django.db import models

class Occupation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    begin_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Reward(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateField()

    def __str__(self):
        return self.name
