# Generated by Django 2.1.7 on 2019-03-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='foyer',
            new_name='household',
        ),
        migrations.AlterField(
            model_name='product',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Commentaire'),
        ),
    ]