from django.shortcuts import render
from . models import Dosen, Mahasiswa, Tenaga_Pendidik

# Create your views here.
def fisip(request):
    dosen = Dosen.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    tenagaPendidik = Tenaga_Pendidik.objects.all()
    context = {
        'dataDosen' : dosen,
        'dataMahasiswa': mahasiswa,
        'dataTenagaPendidik': tenagaPendidik,
    }

    return render(request, 'indexfisip.html', context)