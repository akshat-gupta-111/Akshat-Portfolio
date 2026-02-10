from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=15)
    desc = models.CharField(max_length=500)
    blog_text = models.CharField(max_length=2000)
    media = models.ImageField(upload_to="blogs/")
    def __str__(self):
        return self.title
