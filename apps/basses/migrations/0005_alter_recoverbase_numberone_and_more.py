# Generated by Django 4.0.8 on 2022-10-27 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basses', '0004_alter_finalbase_newgestor_alter_recoverbase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recoverbase',
            name='numberOne',
            field=models.CharField(default='number', max_length=255),
        ),
        migrations.AlterField(
            model_name='recoverbase',
            name='numberTwo',
            field=models.CharField(default='number', max_length=255),
        ),
    ]
