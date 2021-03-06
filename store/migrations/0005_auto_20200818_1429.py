# Generated by Django 3.1 on 2020-08-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200818_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangkeluar',
            name='harga_jual',
            field=models.FloatField(blank=True, db_column='Harga Jual', null=True),
        ),
        migrations.AlterField(
            model_name='barangkeluar',
            name='total',
            field=models.FloatField(blank=True, db_column='Total', null=True),
        ),
        migrations.AlterField(
            model_name='barangmasuk',
            name='harga_beli_field',
            field=models.FloatField(blank=True, db_column='Harga Beli ', null=True),
        ),
        migrations.AlterField(
            model_name='barangmasuk',
            name='total',
            field=models.FloatField(blank=True, db_column='Total', null=True),
        ),
        migrations.AlterField(
            model_name='laporannilaibarang',
            name='rata_harga_beli',
            field=models.FloatField(blank=True, db_column='Rata-Rata Harga Beli', null=True),
        ),
        migrations.AlterField(
            model_name='laporannilaibarang',
            name='total',
            field=models.FloatField(blank=True, db_column='Total', null=True),
        ),
        migrations.AlterField(
            model_name='laporanpenjualan',
            name='harga_beli',
            field=models.FloatField(blank=True, db_column='Harga Beli', null=True),
        ),
        migrations.AlterField(
            model_name='laporanpenjualan',
            name='harga_jual',
            field=models.FloatField(blank=True, db_column='Harga Jual', null=True),
        ),
        migrations.AlterField(
            model_name='laporanpenjualan',
            name='laba',
            field=models.FloatField(blank=True, db_column='Laba', null=True),
        ),
        migrations.AlterField(
            model_name='laporanpenjualan',
            name='total',
            field=models.FloatField(blank=True, db_column='Total', null=True),
        ),
    ]
