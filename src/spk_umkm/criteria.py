"""Definisi kriteria dan pemetaan sub-kriteria ke skor."""
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class SubKriteria:
    label: str
    skor: int

@dataclass(frozen=True)
class Kriteria:
    kode: str
    nama: str
    tipe: str
    sub: List[SubKriteria]

    def skor_dari_label(self, label: str) -> int:
        for item in self.sub:
            if item.label == label:
                return item.skor
        pilihan = ", ".join(self.daftar_label())
        raise ValueError(f"Label '{label}' tidak valid untuk {self.kode}. Pilihan: {pilihan}")

    def daftar_label(self) -> List[str]:
        return [item.label for item in self.sub]

KRITERIA = [
    Kriteria("C1", "Omzet Usaha per Bulan", "benefit", [
        SubKriteria(">10 juta", 5), SubKriteria("7 - 10 juta", 4),
        SubKriteria("4 - 7 juta", 3), SubKriteria("1 - 4 juta", 2),
        SubKriteria("<1 juta", 1),
    ]),
    Kriteria("C2", "Lama Usaha Berjalan", "benefit", [
        SubKriteria(">5 tahun", 5), SubKriteria("3 - 5 tahun", 4),
        SubKriteria("1 - 3 tahun", 3), SubKriteria("6 bulan - 1 tahun", 2),
        SubKriteria("<6 bulan", 1),
    ]),
    Kriteria("C3", "Jumlah Tenaga Kerja", "benefit", [
        SubKriteria(">10 orang", 5), SubKriteria("7 - 10 orang", 4),
        SubKriteria("4 - 6 orang", 3), SubKriteria("1 - 3 orang", 2),
        SubKriteria("Tidak ada (hanya pemilik)", 1),
    ]),
    Kriteria("C4", "Kondisi Tempat Usaha", "benefit", [
        SubKriteria("Milik sendiri, permanen", 5),
        SubKriteria("Milik sendiri, semi permanen", 4),
        SubKriteria("Sewa, permanen", 3),
        SubKriteria("Sewa, semi permanen", 2),
        SubKriteria("Menumpang / tidak tetap", 1),
    ]),
    # Jarak adalah cost secara konsep, tetapi skor sub-kriterianya sudah dibalik.
    # Karena itu seluruh skor diperlakukan sebagai benefit dalam rumus WP.
    Kriteria("C5", "Jarak ke Pusat Pasar/Kota", "cost", [
        SubKriteria("<1 km", 5), SubKriteria("1 - 3 km", 4),
        SubKriteria("3 - 5 km", 3), SubKriteria("5 - 10 km", 2),
        SubKriteria(">10 km", 1),
    ]),
]
KODE_KRITERIA = [k.kode for k in KRITERIA]
NAMA_KRITERIA = [k.nama for k in KRITERIA]
RI_TABLE = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12,
            6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
