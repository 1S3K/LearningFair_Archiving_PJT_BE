# Generated by Django 3.1.1 on 2020-11-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_auto_20201015_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='group',
            field=models.CharField(max_length=3),
        ),
    ]