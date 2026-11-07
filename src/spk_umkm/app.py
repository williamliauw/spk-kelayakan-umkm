"""Antarmuka menu interaktif aplikasi SPK."""
from pathlib import Path
import numpy as np
from .criteria import KRITERIA, KODE_KRITERIA
from .models import Alternatif
from .sample_data import data_contoh
from .ahp import hitung_ahp, matriks_ahp_default
from .weighted_product import hitung_wp
from .reporting import cetak_tabel, laporan_ahp, laporan_wp
from .visualization import grafik_ascii, buat_grafik
from .export import ekspor_hasil

class AplikasiSPK:
    def __init__(self):
        self.alternatif = data_contoh()
        self.matriks_ahp = matriks_ahp_default()
        self.hasil_ahp = None
        self.hasil_wp = None

    def invalidasi_hasil(self):
        self.hasil_ahp = None
        self.hasil_wp = None

    def lihat_alternatif(self):
        rows = [[i, alt.nama] + [alt.nilai.get(k, "-") for k in KODE_KRITERIA]
                for i, alt in enumerate(self.alternatif, 1)]
        cetak_tabel(rows, ["No", "Nama UMKM"] + KODE_KRITERIA)

    def tambah_alternatif(self):
        nama = input("Nama UMKM: ").strip()
        if not nama:
            print("Nama tidak boleh kosong."); return
        if any(a.nama.casefold() == nama.casefold() for a in self.alternatif):
            print("Nama UMKM sudah terdaftar."); return
        nilai = {}
        for k in KRITERIA:
            print(f"\n{k.kode} - {k.nama}")
            for i, label in enumerate(k.daftar_label(), 1):
                print(f"{i}. {label}")
            while True:
                pilihan = input("Pilih nomor: ").strip()
                if pilihan.isdigit() and 1 <= int(pilihan) <= len(k.sub):
                    nilai[k.kode] = k.sub[int(pilihan)-1].label
                    break
                print("Pilihan tidak valid.")
        self.alternatif.append(Alternatif(nama, nilai))
        self.invalidasi_hasil()
        print("Alternatif berhasil ditambahkan.")

    def edit_alternatif(self):
        self.lihat_alternatif()
        pilihan = input("Nomor UMKM yang diubah (0 batal): ").strip()
        if not pilihan.isdigit() or not 1 <= int(pilihan) <= len(self.alternatif):
            print("Tidak ada perubahan.")
            return
        alt = self.alternatif[int(pilihan) - 1]
        nama_baru = input(f"Nama baru [{alt.nama}]: ").strip()
        if nama_baru:
            if any(a is not alt and a.nama.casefold() == nama_baru.casefold()
                   for a in self.alternatif):
                print("Nama tersebut sudah digunakan.")
                return
            alt.nama = nama_baru
        for kriteria in KRITERIA:
            print(f"\nNilai saat ini untuk {kriteria.kode}: {alt.nilai[kriteria.kode]}")
            ubah = input(f"Ubah nilai {kriteria.nama}? [y/N]: ").strip().lower()
            if ubah == "y":
                for nomor, label in enumerate(kriteria.daftar_label(), 1):
                    print(f"{nomor}. {label}")
                while True:
                    nilai = input("Pilih nomor: ").strip()
                    if nilai.isdigit() and 1 <= int(nilai) <= len(kriteria.sub):
                        alt.nilai[kriteria.kode] = kriteria.sub[int(nilai)-1].label
                        break
                    print("Pilihan tidak valid.")
        self.invalidasi_hasil()
        print("Data UMKM berhasil diperbarui.")

    def hapus_alternatif(self):
        self.lihat_alternatif()
        pilihan = input("Nomor yang dihapus (0 batal): ").strip()
        if pilihan.isdigit() and 1 <= int(pilihan) <= len(self.alternatif):
            del self.alternatif[int(pilihan)-1]
            self.invalidasi_hasil()
            print("Data berhasil dihapus.")
        else:
            print("Tidak ada perubahan.")

    def jalankan_ahp(self):
        self.hasil_ahp = hitung_ahp(self.matriks_ahp)
        self.hasil_wp = None
        laporan_ahp(self.hasil_ahp)

    def jalankan_wp(self):
        if not self.alternatif:
            print("Belum ada alternatif UMKM."); return
        if self.hasil_ahp is None:
            self.jalankan_ahp()
        self.hasil_wp = hitung_wp(self.alternatif, self.hasil_ahp.bobot)
        laporan_wp(self.hasil_wp, self.hasil_ahp.bobot)

    def atur_matriks(self):
        print("\n" + "=" * 58)
        print("PANDUAN SKALA PERBANDINGAN AHP")
        print("=" * 58)
        print("1. Nilai 1 berarti kedua kriteria sama penting.")
        print("2. Nilai 3 berarti kriteria pertama sedikit lebih penting.")
        print("3. Nilai 5 berarti kriteria pertama lebih penting.")
        print("4. Nilai 7 berarti kriteria pertama sangat lebih penting.")
        print("5. Nilai 9 berarti kriteria pertama mutlak lebih penting.")
        print("\nNilai 2, 4, 6, dan 8 dapat digunakan sebagai nilai antara.")
        print("Jika kriteria kedua lebih penting, gunakan nilai kebalikan.")
        print("Contoh: 0.3333 berarti kriteria kedua sedikit lebih penting.")
        print("Ketik 'batal' kapan saja untuk kembali ke menu utama.")
        print("=" * 58)

        print("\nMasukkan nilai perbandingan untuk bagian segitiga atas.")
        print("Gunakan angka positif. Contoh: 3.")
        matriks = np.ones((len(KRITERIA), len(KRITERIA)))

        for i in range(len(KRITERIA)):
            for j in range(i + 1, len(KRITERIA)):
                while True:
                    masukan = input(
                        f"{KRITERIA[i].kode} dibanding {KRITERIA[j].kode} "
                        "(atau 'batal'): "
                    ).strip().lower()

                    if masukan == "batal":
                        print("Pengaturan matriks dibatalkan. Matriks sebelumnya tetap digunakan.")
                        return

                    try:
                        nilai = float(masukan)
                        if not np.isfinite(nilai) or nilai <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Masukkan angka positif yang valid, atau ketik 'batal'.")

                matriks[i, j] = nilai
                matriks[j, i] = 1 / nilai

        self.matriks_ahp = matriks
        self.invalidasi_hasil()
        print("Matriks diperbarui. Jalankan AHP untuk menghitung bobot baru.")

    def tampilkan_grafik(self):
        if self.hasil_wp is None:
            print("Jalankan WP terlebih dahulu."); return
        print(grafik_ascii(self.hasil_wp))
        path = Path("outputs/hasil_peringkat.png")
        hasil = buat_grafik(self.hasil_wp, path)
        print(f"Grafik disimpan: {hasil}" if hasil else "Matplotlib belum tersedia.")

    def ekspor(self):
        if self.hasil_ahp is None or self.hasil_wp is None:
            print("Jalankan AHP dan WP terlebih dahulu."); return
        hasil = ekspor_hasil(self.alternatif, self.hasil_ahp, self.hasil_wp,
                             "outputs/hasil_spk_umkm.xlsx")
        print(f"Hasil ekspor: {hasil}")

    def menu(self):
        aksi = {
            "1": self.lihat_alternatif, "2": self.tambah_alternatif,
            "3": self.edit_alternatif, "4": self.hapus_alternatif,
            "5": self.jalankan_ahp,
            "6": self.jalankan_wp, "7": self.tampilkan_grafik,
            "8": self.ekspor, "9": self.atur_matriks,
        }
        while True:
            print("""
========================================================
 SPK KELAYAKAN PENERIMA BANTUAN UMKM (AHP - WP)
========================================================
1. Lihat data UMKM
2. Tambah UMKM
3. Ubah data UMKM
4. Hapus UMKM
5. Hitung bobot AHP
6. Hitung peringkat WP
7. Tampilkan grafik
8. Ekspor hasil
9. Atur matriks AHP
0. Keluar
""")
            pilihan = input("Pilih menu: ").strip()
            if pilihan == "0":
                print("Program selesai."); break
            fungsi = aksi.get(pilihan)
            if fungsi:
                try:
                    fungsi()
                except (ValueError, OSError) as error:
                    print(f"Terjadi kesalahan: {error}")
            else:
                print("Pilihan tidak dikenal.")
