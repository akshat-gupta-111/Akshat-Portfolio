from django.db import models


# Create your models here.
class CertificateCard(models.Model):
    title = models.CharField(max_length=15)
    desc = models.CharField(max_length=500)
    verify = models.CharField(max_length=500)
    media = models.ImageField(upload_to="certificates/")
    link = models.CharField(max_length=500)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
