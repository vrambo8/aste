# Generated by Django 2.0.7 on 2018-10-02 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20181002_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inserzione',
            name='id',
            field=models.CharField(default='dMwoMYhFyiiwL6TDWC3hCH', max_length=15, primary_key=True, serialize=False),
        ),
    ]
