from django.db import models
from datetime import date
# Create your models here.
class Achievements(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="achievements/")
    desc = models.CharField(max_length=2000)
    date = models.DateField(default=date.today)
    link = models.CharField(max_length=500)
    is_available = models.BooleanField(default=False)
