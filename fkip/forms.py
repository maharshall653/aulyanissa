from django.forms import ModelForm
from fkip.models import Dosen
from fkip.models import Tenaga_Pendidik
from fkip.models import Mahasiswa
from django import forms

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'

        widgets = {
            'nip' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggal_lahir' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
            'photo' : forms.TextInput({'class':'form-control'}),
        }

class FormTenaga_Pendidik(ModelForm):
    class Meta:
        model = Tenaga_Pendidik
        fields = '__all__'

        widgets = {
            'nip' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggal_Lahir' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'unit' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
            'photo' : forms.TextInput({'class':'form-control'}),
        }

class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'

        widgets = {
            'nim' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggal_lahir' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
            'photo' : forms.TextInput({'class':'form-control'}),
        }