# Generated by Django 2.0.7 on 2018-10-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inserzione',
            options={'verbose_name': 'insertion', 'verbose_name_plural': 'insertions'},
        ),
        migrations.AlterField(
            model_name='inserzione',
            name='id',
            field=models.CharField(default='EsQyhb7A3CWz9V3mE4sEde', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='partita_iva',
            field=models.CharField(max_length=50),
        ),
    ]