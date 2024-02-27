# Generated by Django 4.2.5 on 2024-02-27 08:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='base_distance_in_km',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='fix_price',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='item',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='km_price',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='organization',
        ),
        migrations.AddField(
            model_name='pricing',
            name='item_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricing',
            name='organization_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricing',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.5, max_digits=6),
        ),
    ]
