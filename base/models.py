from django.db import models

class Conference(models.Model):
    naimenovanie = models.CharField(max_length=250)
    uchregdenie = models.CharField(max_length=250)
    strana = models.CharField(max_length=30)
    status_meropriatia = models.CharField(max_length=20)
    status_uchastnikov = models.CharField(max_length=40)
    data_podachi = models.DateField(verbose_name="Data Podachia")
    data_provedenia = models.DateField()
    primechanie = models.CharField(max_length=250)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

class Podpiska(models.Model):
    email = models.EmailField()