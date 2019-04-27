# Generated by Django 2.1.7 on 2019-03-23 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20190323_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='achatop',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='achatop',
            name='household',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Household'),
        ),
        migrations.AlterField(
            model_name='achatop',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='referent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Member', verbose_name='Référent'),
        ),
    ]