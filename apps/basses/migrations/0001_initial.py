# Generated by Django 4.0.8 on 2022-10-27 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='finalBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.IntegerField()),
                ('name', models.CharField(default='user', max_length=255)),
                ('numberOne', models.IntegerField()),
                ('numberTwo', models.IntegerField()),
                ('observation', models.CharField(max_length=400)),
                ('line', models.CharField(max_length=255)),
                ('account', models.IntegerField()),
                ('gestor', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('newGestor', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Names',
            fields=[
                ('document', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='user', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='recoverBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.IntegerField()),
                ('name', models.CharField(default='user', max_length=255)),
                ('numberOne', models.IntegerField()),
                ('numberTwo', models.IntegerField()),
                ('observation', models.CharField(max_length=400)),
                ('line', models.CharField(max_length=255)),
                ('account', models.IntegerField()),
                ('gestor', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rols',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rol_name', models.CharField(default='ADMIN', max_length=255)),
                ('spanish_name', models.CharField(default='ADMINISTRADOR', max_length=255)),
            ],
        ),
    ]
