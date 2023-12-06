# Generated by Django 4.1.13 on 2023-12-02 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=80)),
                ('pais', models.CharField(max_length=70)),
                ('titulos', models.PositiveIntegerField()),
                ('fundado', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('resultado', models.CharField(max_length=50)),
                ('encuentros', models.CharField(max_length=100)),
                ('analisis', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('perteneceid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbol.equipos')),
            ],
        ),
    ]
