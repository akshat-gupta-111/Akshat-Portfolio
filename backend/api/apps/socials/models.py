from django.db import models


# Create your models here.
class SocialCard(models.Model):
    title = models.CharField(max_length=15)
    text = models.CharField(max_length=30)
    media = models.ImageField(upload_to="socials/")
    link = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
