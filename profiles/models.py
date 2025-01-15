from django.db import models


# Create your models here.
class UserProfile(models.Model):
    # Se creara una subcarpeta (images) dentro de la caperta raiz "uploads"
    # Antes se usaba:
    #  image = models.FileField(upload_to="images")
    image = models.ImageField(upload_to="images")
