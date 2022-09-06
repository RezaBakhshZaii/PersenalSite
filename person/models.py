from django.db import models


# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='static/image')
    progress = models.IntegerField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/image')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Information(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/image')
    descriptions = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class Messages(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    description = models.CharField(max_length=40)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return f"name : {self.name}  (description: {self.description})"
