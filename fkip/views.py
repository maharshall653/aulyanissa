from django.shortcuts import render, redirect
from . models import Dosen, Mahasiswa, Tenaga_Pendidik
from fkip.forms import FormDosen, FormDosen, FormTenaga_Pendidik, FormMahasiswa
from django.contrib import messages 

def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen)
    dosen.delete()
    if request.method == "POST":
        dosen.hapus()
    
    return redirect('/fkip/')

def ubah_dosen(request, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('ubah_dosen', id_dosen=id_dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }
    return render(request, template, konteks)

def hapus_tenagapendidik(request, id_tenagapendidik):
    tenagapendidik = Tenagapendidik.objects.filter(id=id_tenagapendidik)
    tenagapendidik.delete()
    if request.method == "POST":
        tenagapendidik.hapus()
    
    return redirect('/fkip/')

def ubah_tenagapendidik(request, id_tenagapendidik):
    tenagapendidik = Tenaga_Pendidik.objects.get(id=id_tenagapendidik)
    template = 'ubah-tenagapendidik.html'
    if request.POST:
        form = FormTenaga_Pendidik(request.POST, instance=tenagapendidik)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('ubah_tenagapendidik', id_tenagapendidik=id_tenagapendidik)
    else:
        form = FormTenaga_Pendidik(instance=tenagaPendidik)
        konteks = {
            'form':form,
            'tenagapendidik':Tenaga_Pendidik,
        }
    return render(request, template, konteks)

def hapus_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.filter(id=id_mahasiswa)
    mahasiswa.delete()
    if request.method == "POST":
        mahasiswa.hapus()
    
    return redirect('/fkip/')

def ubah_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(ubah_mahasiswa, id_mahasiswa=id_mahasiswa)
    else:
        form = FormMahasiswa(instance=mahasiswa)
        konteks = {
            'form':form,
            'mahasiswa':mahasiswa,
        }
    return render(request, template, konteks)

# Create your views here.
def fkip(request):
    dosen = Dosen.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    tenagaPendidik = Tenaga_Pendidik.objects.all()
    context = {
        'dataDosen' : dosen,
        'dataMahasiswa': mahasiswa,
        'dataTenagaPendidik': tenagaPendidik,
    }
    
    return render(request, 'indexfkip.html', context)

def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)
    else:
        form = FormDosen()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-dosen.html', konteks)

def tambah_tenagapendidik(request):
    if request.POST:
        form = FormTenagaPendidik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTenagaPendidik()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-tenagapendidik.html', konteks)
    else:
        form = FormTenaga_Pendidik()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-tenagapendidik.html', konteks)

def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-mahasiswa.html', konteks)
    else:
        form = FormMahasiswa()

        konteks = {
            'form' : form,
        }

    return render(request, 'tambah-mahasiswa.html', konteks)