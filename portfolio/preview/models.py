from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    tags = models.CharField(max_length=40)
    image = models.FileField(upload_to='img/')