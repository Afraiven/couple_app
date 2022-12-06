from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

def unique_rand():
    while True:
        code = password = User.objects.make_random_password(length=8)
        if not Tekst.objects.filter(code=code).exists():
            return code

class Tekst(models.Model):
    tekst = models.CharField(max_length=300)
    seen = models.IntegerField(default=0)
    opened_date = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=300, default=unique_rand)
    image = models.CharField(max_length=300, blank=True, null=True)
    image2 = models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.tekst


class Daily(models.Model):
    today = models.DateTimeField(default=datetime.now(), blank=True)
    counter = models.IntegerField(default=3)
    def __str__(self):
        return str(self.today)