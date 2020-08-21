from django.contrib import admin
from .models import JumlahBarang, BarangMasuk, BarangKeluar, LaporanPenjualan, LaporanNilaiBarang
from .paginator import TimeLimitedPaginator
import sys


# Register your models here.
# admin.site.register(JumlahBarang)
# admin.site.register(BarangMasuk)
# admin.site.register(BarangKeluar)


@admin.register(JumlahBarang)
class JBAdmin(admin.ModelAdmin):
    list_display = ("sku", "nama_item", "jumlah_sekarang")
    list_filter = ("sku", "nama_item",)
    search_fields = ("sku", "nama_item",)


@admin.register(BarangMasuk)
class BMAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'waktu_field',
        'sku',
        'nama_barang',
        'jumlah_pemesanan',
        'jumlah_diterima',
        'harga_beli_field',
        'total',
        'nomer_kwitansi',
        'catatan',
    )
    list_filter = (
        'waktu_field',
        'sku',
        'nama_barang',
    )
    search_fields = (
        'waktu_field',
        'sku',
        'nama_barang',
    )


@admin.register(BarangKeluar)
class BKAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'waktu_field',
        'sku',
        'nama_barang',
        'jumlah_keluar',
        'harga_jual',
        'total',
        'catatan',
    )
    list_filter = (
        'waktu_field',
        'sku',
        'nama_barang',
    )
    search_fields = (
        'waktu_field',
        'sku',
        'nama_barang',
    )


@admin.register(LaporanNilaiBarang)
class LNBAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sku',
        'nama_item',
        'jumlah',
        'rata_harga_beli',
        'total',
    )
    list_filter = (
        'sku',
        'nama_item',
    )
    search_fields = (
        'sku',
        'nama_item',
    )


@admin.register(LaporanPenjualan)
class LPAdmin(admin.ModelAdmin):
    list_display = (
        'id_pesanan',
        'waktu_field',
        'sku',
        'nama_barang',
        'jumlah',
        'harga_jual',
        'total',
        'harga_beli',
        'laba',
    )
    list_filter = (
        'id_pesanan',
        'sku',
        'nama_barang',
    )
    search_fields = (
        'id_pesanan',
        'sku',
        'nama_barang',
    )
