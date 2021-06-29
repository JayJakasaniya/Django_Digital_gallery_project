from django.db import models

# Create your models here.


class gallery(models.Model):
    Title = models.CharField(max_length=100, null='True')
    Decriptions = models.CharField(max_length=200, null='True')
    DrawingImage = models.ImageField()

    def __str__(self):
        return (self.Title)


class contacts(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return (self.name)
