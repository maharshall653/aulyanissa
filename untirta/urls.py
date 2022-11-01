"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from faperta.views import faperta 
from feb.views import feb
from fh.views import fh
from fisip.views import fisip 
from fk.views import fk 
from fkip.views import fkip
from fkip.views import *
from ft.views import ft
from pascasarjana.views import pascasarjana
from profil.views import profil
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('faperta/', faperta),
    path('feb/', feb),
    path('fh/', fh),
    path('fisip/', fisip), 
    path('fk/', fk),
    path('fkip/', fkip),
    path('ft/', ft),
    path('pascasarjana/', pascasarjana),
    path('profil/', profil),
    path('tambah-dosen/', tambah_dosen, name='tambah_dosen'),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'),
    path('dosen/hapus/<int:id_dosen>', hapus_dosen, name='hapus_dosen'),
    path('tambah-tenagapendidik//', tambah_tenagapendidik, name='tambah_tenagapendidik'),
    path('tenagapendidik/ubah/<int:id_tenagapendidik>', ubah_tenagapendidik, name='ubah_tenagapendidik'),
    path('tenagapendidik/hapus/<int:id_tenagapendidik>', hapus_tenagapendidik, name='hapus_tenagapendidik'),
    path('tambah-mahasiswa/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name='hapus_mahasiswa'),
]
