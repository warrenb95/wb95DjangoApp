# Generated by Django 2.1.5 on 2019-02-15 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0006_auto_20190212_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='gallery_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_image', to='photography.GalleryGroup'),
        ),
    ]
