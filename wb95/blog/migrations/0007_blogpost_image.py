# Generated by Django 2.1.5 on 2019-02-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190215_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='', upload_to='images/blog/photography'),
        ),
    ]