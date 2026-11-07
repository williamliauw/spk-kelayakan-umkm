"""Dataset contoh sintetis untuk demonstrasi."""
from .models import Alternatif

def data_contoh():
    return [
        Alternatif("Warung Bu Yati", {
            "C1": "4 - 7 juta", "C2": "3 - 5 tahun", "C3": "1 - 3 orang",
            "C4": "Sewa, permanen", "C5": "1 - 3 km"}),
        Alternatif("Konveksi Pak Hamid", {
            "C1": ">10 juta", "C2": ">5 tahun", "C3": "7 - 10 orang",
            "C4": "Milik sendiri, permanen", "C5": "3 - 5 km"}),
        Alternatif("Bengkel Motor Jaya", {
            "C1": "7 - 10 juta", "C2": "1 - 3 tahun", "C3": "4 - 6 orang",
            "C4": "Sewa, semi permanen", "C5": "<1 km"}),
        Alternatif("Toko Kelontong Mekar", {
            "C1": "1 - 4 juta", "C2": "<6 bulan",
            "C3": "Tidak ada (hanya pemilik)",
            "C4": "Menumpang / tidak tetap", "C5": "5 - 10 km"}),
        Alternatif("Usaha Kerupuk Ibu Sri", {
            "C1": "4 - 7 juta", "C2": "1 - 3 tahun", "C3": "1 - 3 orang",
            "C4": "Milik sendiri, semi permanen", "C5": "1 - 3 km"}),
    ]
