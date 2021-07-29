from django.db import models
import uuid
from django.utils import timezone


# Create your models here.

class IP(models.Model):
    ip = models.GenericIPAddressField()
    ora_data = models.DateTimeField(default=timezone.now)

class Utilizator(models.Model):
    nume = models.CharField(max_length=100)
    email = models.EmailField()
    cod_secret = models.UUIDField(default=uuid.uuid4())
    prima_logare = models.DateTimeField(default=timezone.now)
    ultima_logare = models.DateTimeField(default=timezone.now)
    ipuri = models.ManyToManyField(IP, blank=True)