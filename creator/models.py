from django.db import models


class Curriculum(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    file = models.FileField(upload_to='cvs')
    nickname = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
