# Generated by Django 2.2.6 on 2019-11-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_localsettings_use_exports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approcompteop',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='changestockop',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mail',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
