# Generated by Django 4.1.7 on 2023-02-20 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_artiles_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artiles',
            new_name='Articles',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='titli',
            new_name='title',
        ),
    ]
