"""Perhitungan Analytical Hierarchy Process (AHP)."""
import numpy as np
from .criteria import RI_TABLE
from .models import HasilAHP

def matriks_ahp_default():
    return np.array([
        [1, 3, 5, 5, 7],
        [1/3, 1, 3, 3, 5],
        [1/5, 1/3, 1, 1, 3],
        [1/5, 1/3, 1, 1, 3],
        [1/7, 1/5, 1/3, 1/3, 1],
    ], dtype=float)

def validasi_matriks(matriks):
    matriks = np.asarray(matriks, dtype=float)
    if matriks.ndim != 2 or matriks.shape[0] != matriks.shape[1]:
        raise ValueError("Matriks AHP harus berbentuk persegi.")
    if matriks.shape[0] < 1:
        raise ValueError("Matriks AHP tidak boleh kosong.")
    if not np.isfinite(matriks).all() or (matriks <= 0).any():
        raise ValueError("Seluruh nilai matriks harus berupa angka positif dan terbatas.")
    if not np.allclose(np.diag(matriks), 1.0):
        raise ValueError("Diagonal matriks AHP harus bernilai 1.")
    if not np.allclose(matriks * matriks.T, 1.0, atol=1e-8):
        raise ValueError("Matriks harus resiprokal: a[i,j] = 1 / a[j,i].")
    return matriks

def hitung_ahp(matriks):
    matriks = validasi_matriks(matriks)
    n = matriks.shape[0]
    jumlah_kolom = matriks.sum(axis=0)
    matriks_normal = matriks / jumlah_kolom
    bobot = matriks_normal.mean(axis=1)

    if np.any(bobot <= 0):
        raise ValueError("Bobot AHP harus bernilai positif.")

    vektor_terbobot = matriks @ bobot
    lambda_max = float(np.mean(vektor_terbobot / bobot))
    ci = (lambda_max - n) / (n - 1) if n > 1 else 0.0
    ri = RI_TABLE.get(n, 1.49)
    cr = ci / ri if ri > 0 else 0.0
    return HasilAHP(matriks, matriks_normal, bobot, lambda_max,
                    float(ci), float(ri), float(cr), bool(cr <= 0.10))
