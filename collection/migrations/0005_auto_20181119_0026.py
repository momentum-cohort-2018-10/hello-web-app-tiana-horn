# Generated by Django 2.1.3 on 2018-11-19 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20181118_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pictures',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]