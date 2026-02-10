from django.db import models


# Create your models here.
class SiteSettings(models.Model):
    title = models.CharField(max_length=15)
    heading = models.CharField(max_length=30)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15, default='')
    desc = models.CharField(max_length=500)

    my_pic = models.ImageField(upload_to="home/")
    background = models.ImageField(upload_to="home/")

    resume = models.FileField(upload_to="home/")
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title
