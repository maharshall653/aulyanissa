# Generated by Django 4.1 on 2022-10-04 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fkip', '0003_tenaga_pendidik'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosen',
            name='photo',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='photo',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tenaga_pendidik',
            name='photo',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
