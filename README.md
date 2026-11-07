# SPK Kelayakan Penerima Bantuan UMKM (AHP-WP)

Aplikasi Python berbasis terminal untuk membantu pemeringkatan alternatif UMKM
berdasarkan lima kriteria menggunakan metode **Analytical Hierarchy Process
(AHP)** dan **Weighted Product (WP)**.

## Fitur
- Pengelolaan alternatif UMKM (lihat, tambah, ubah, hapus).
- Matriks perbandingan berpasangan AHP.
- Perhitungan bobot dan uji konsistensi CI/CR.
- Perhitungan nilai S, nilai V, dan peringkat WP.
- Grafik peringkat dalam format PNG.
- Ekspor hasil ke Excel atau CSV.
- Mode demo tanpa input manual.
- Unit test untuk fungsi inti AHP dan WP.

## Struktur Proyek
```text
spk-kelayakan-umkm/
├── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── src/spk_umkm/
│   ├── ahp.py
│   ├── app.py
│   ├── criteria.py
│   ├── export.py
│   ├── models.py
│   ├── reporting.py
│   ├── sample_data.py
│   ├── visualization.py
│   └── weighted_product.py
├── tests/
├── data/
├── docs/
└── outputs/
```

## Persyaratan
- Python 3.9 atau lebih baru.
- NumPy dan Pandas.
- Matplotlib untuk grafik PNG.
- OpenPyXL untuk ekspor Excel.
- Tabulate untuk tabel terminal yang lebih rapi.

## Instalasi
Disarankan menggunakan virtual environment.

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Instal dependensi:
```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Menjalankan
Menu interaktif:
```bash
python main.py
```

Simulasi otomatis:
```bash
python main.py --demo
```

Hasil grafik dan laporan disimpan di folder `outputs/`.

## Menjalankan Pengujian
```bash
python -m unittest discover -s tests -v
```

## Metodologi
Penjelasan ringkas metode dapat dibaca pada [`docs/metodologi.md`](docs/metodologi.md).
Cara membaca hasil tersedia pada [`docs/hasil-analisis.md`](docs/hasil-analisis.md).

## Catatan Data dan Penggunaan
Data bawaan adalah data ilustrasi/sintetis, bukan data penerima bantuan nyata. Salinan CSV tersedia di `data/umkm_sample.csv`.
Hasil sistem merupakan rekomendasi berbasis masukan dan perlu ditinjau bersama
validasi lapangan serta kebijakan yang berlaku.

## Pengembangan
Proyek ini merupakan implementasi pembelajaran SPK. Bobot, kriteria, dan
pemetaan sub-kriteria dapat disesuaikan dengan kebutuhan studi kasus.
