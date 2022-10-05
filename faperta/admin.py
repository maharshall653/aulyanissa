from django.contrib import admin

from .models import Dosen, Mahasiswa, Tenaga_Pendidik

# Register your models here.
admin.site.register(Dosen)
admin.site.register(Tenaga_Pendidik)
admin.site.register(Mahasiswa)