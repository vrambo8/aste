# Generated by Django 2.1.3 on 2018-11-22 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_auto_20181121_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inserzione',
            name='id',
            field=models.CharField(default='HY3agATD5BvLLw6k3xsJUW', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
