from django.db import models

# Create your models here.
class Dosen(models.Model):
    nip = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    alamat = models.TextField()
    photo = models.CharField(max_length=500, null=True)

class Tenaga_Pendidik(models.Model):
    nip = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    alamat = models.CharField(max_length=200)
    photo = models.CharField(max_length=500, null=True)

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    photo = models.CharField(max_length=500, null=True)


