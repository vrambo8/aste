# Generated by Django 2.1.3 on 2018-11-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20181101_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inserzione',
            name='id',
            field=models.CharField(default='WiJCEAkzzLuFUA5dxGn7td', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]