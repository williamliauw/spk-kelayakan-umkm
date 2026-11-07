"""Model data untuk alternatif UMKM dan hasil perhitungan."""
from dataclasses import dataclass
from typing import Dict
from .criteria import KRITERIA

@dataclass
class Alternatif:
    nama: str
    nilai: Dict[str, str]

    def ke_skor(self) -> Dict[str, int]:
        if not self.nama.strip():
            raise ValueError("Nama UMKM tidak boleh kosong.")
        hasil = {}
        for kriteria in KRITERIA:
            label = self.nilai.get(kriteria.kode)
            if label is None:
                raise ValueError(f"Alternatif '{self.nama}' belum memiliki nilai {kriteria.kode}.")
            hasil[kriteria.kode] = kriteria.skor_dari_label(label)
        return hasil

@dataclass
class HasilAHP:
    matriks: object
    matriks_normal: object
    bobot: object
    lambda_max: float
    ci: float
    ri: float
    cr: float
    konsisten: bool

@dataclass
class BarisWP:
    nama: str
    skor: Dict[str, int]
    s: float
    v: float
    peringkat: int = 0
