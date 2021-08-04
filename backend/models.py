from django.db import models
import uuid
from django.utils import timezone

class IP(models.Model):
    ip = models.GenericIPAddressField()
    ora_data = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.ip)

class Utilizator(models.Model):
    nume = models.CharField(max_length=100)
    parola = models.CharField(max_length=100, default=str(uuid.uuid4()))
    cod_secret = models.CharField(max_length=100, default=str(uuid.uuid4()))
    prima_logare = models.DateTimeField(default=timezone.now)
    ultima_logare = models.DateTimeField(default=timezone.now)
    ipuri = models.ManyToManyField(IP, blank=True)
    acceptat = models.BooleanField(default=True)
    def __str__(self):
        return str(self.nume)

class Executabil(models.Model):
    program = models.FileField(upload_to='programe/%Y/%m/%d/')
    ora_data_upload = models.DateTimeField(default=timezone.now)
    tip_executabil = models.SmallIntegerField(default=1)
    def __str__(self):
        return (str(self.program)).replace("/","-")