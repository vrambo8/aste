# Generated by Django 2.0.7 on 2018-11-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20181009_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='inserzione',
            name='immagine',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='inserzione',
            name='descrizione',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='inserzione',
            name='id',
            field=models.CharField(default='yYnqRDtMtoo2AhvM2mcLnC', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='inserzione',
            name='indirizzo',
            field=models.CharField(default='', max_length=50),
        ),
    ]