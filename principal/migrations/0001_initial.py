# Generated by Django 4.2.21 on 2025-07-17 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('idHorario', models.AutoField(primary_key=True, serialize=False)),
                ('hora_entrada', models.CharField(max_length=20)),
                ('hora_salida', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('idpieza', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_serie', models.CharField(max_length=100, unique=True)),
                ('ubicacion', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('idSolicitud', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=255)),
                ('pieza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.inventario')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('idmovimiento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=25)),
                ('cantidad', models.IntegerField()),
                ('motivo', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pieza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.inventario')),
            ],
        ),
        migrations.CreateModel(
            name='AlertaHorario',
            fields=[
                ('idalerta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('rol', models.CharField(max_length=255)),
                ('ip_dispositivo', models.CharField(max_length=255)),
                ('motivo', models.CharField(max_length=255)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
