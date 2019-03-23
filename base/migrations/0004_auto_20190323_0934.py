# Generated by Django 2.1.7 on 2019-03-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_member_receipt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achatop',
            old_name='member',
            new_name='household',
        ),
        migrations.RenameField(
            model_name='approcompteop',
            old_name='member',
            new_name='household',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='household',
            name='account',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Solde du compte'),
        ),
        migrations.AlterField(
            model_name='household',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Commentaire'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='member',
            name='receipt',
            field=models.BooleanField(default=True, verbose_name='Recevoir un ticket de caisse par mail ?'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Commentaire (quel Gasier a été en contact, historique des échages, ...)'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='contact',
            field=models.TextField(blank=True, verbose_name='Mail / téléphone / adresse du fournisseur'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nom'),
        ),
    ]
