"""Perhitungan Weighted Product (WP)."""
from .criteria import KRITERIA
from .models import BarisWP

def hitung_vektor_s(alternatif, bobot):
    if len(alternatif) == 0:
        raise ValueError("Minimal harus ada satu alternatif UMKM.")
    if len(bobot) != len(KRITERIA):
        raise ValueError("Jumlah bobot harus sama dengan jumlah kriteria.")
    if any(float(w) <= 0 for w in bobot):
        raise ValueError("Seluruh bobot harus positif.")

    hasil = []
    for alt in alternatif:
        skor = alt.ke_skor()
        nilai_s = 1.0
        for indeks, kriteria in enumerate(KRITERIA):
            # Semua skor menjadi benefit karena arah cost C5 sudah dibalik
            # pada pemetaan sub-kriteria.
            nilai_s *= skor[kriteria.kode] ** float(bobot[indeks])
        hasil.append((alt, skor, nilai_s))
    return hasil

def hitung_wp(alternatif, bobot):
    data_s = hitung_vektor_s(alternatif, bobot)
    total_s = sum(item[2] for item in data_s)
    if total_s <= 0:
        raise ValueError("Total vektor S harus lebih besar dari nol.")
    baris = [BarisWP(alt.nama, skor, nilai_s, nilai_s / total_s)
             for alt, skor, nilai_s in data_s]
    baris.sort(key=lambda item: item.v, reverse=True)
    for peringkat, item in enumerate(baris, start=1):
        item.peringkat = peringkat
    return baris
