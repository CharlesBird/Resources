# Generated by Django 2.1.7 on 2019-03-25 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_auto_20190325_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockbasic',
            name='enname',
            field=models.CharField(max_length=128, verbose_name='英文全称'),
        ),
    ]