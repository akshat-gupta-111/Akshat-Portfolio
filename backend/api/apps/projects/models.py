from django.db import models


# Create your models here.
class ProjectCard(models.Model):
    title = models.CharField(max_length=15)
    desc = models.CharField(max_length=500)
    git_link = models.CharField(max_length=500)
    media = models.ImageField(upload_to="projects/")
    live_link = models.CharField(max_length=500)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title
