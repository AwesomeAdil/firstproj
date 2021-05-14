from django.db import models
from django.conf import settings
from django.utils import timezone



class Logger(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True, null = True)
    created_date = models.DateTimeField(default=timezone.now)
    number = models.IntegerField(blank=True, null = True)


    def __str__(self):
        return self.name