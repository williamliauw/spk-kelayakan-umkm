"""Fungsi penyajian hasil ke terminal."""
from .criteria import KRITERIA, KODE_KRITERIA, NAMA_KRITERIA

try:
    from tabulate import tabulate
except ImportError:
    tabulate = None

def cetak_tabel(data, headers):
    if tabulate:
        print(tabulate(data, headers=headers, tablefmt="simple_grid", floatfmt=".4f"))
    else:
        print(" | ".join(map(str, headers)))
        for row in data:
            print(" | ".join(map(str, row)))

def laporan_ahp(hasil):
    print("\n" + "=" * 72)
    print("HASIL AHP - PEMBOBOTAN KRITERIA")
    print("=" * 72)
    cetak_tabel([[NAMA_KRITERIA[i]] + list(hasil.matriks[i])
                 for i in range(len(KRITERIA))], ["Kriteria"] + KODE_KRITERIA)
    print("\nBobot prioritas:")
    cetak_tabel([[KODE_KRITERIA[i], NAMA_KRITERIA[i],
                  f"{hasil.bobot[i]:.4f}", f"{hasil.bobot[i]*100:.2f}%"]
                 for i in range(len(KRITERIA))],
                ["Kode", "Kriteria", "Bobot", "Persentase"])
    print(f"Lambda max: {hasil.lambda_max:.4f}")
    print(f"CI: {hasil.ci:.4f} | RI: {hasil.ri:.4f} | CR: {hasil.cr:.4f}")
    print("Status:", "KONSISTEN" if hasil.konsisten else "TIDAK KONSISTEN")

def laporan_wp(baris, bobot):
    print("\n" + "=" * 72)
    print("HASIL WP - PERINGKAT ALTERNATIF UMKM")
    print("=" * 72)
    cetak_tabel([[item.peringkat, item.nama] +
                 [item.skor[k] for k in KODE_KRITERIA] +
                 [f"{item.s:.4f}", f"{item.v:.4f}"] for item in baris],
                ["Rank", "Alternatif"] + KODE_KRITERIA + ["Nilai S", "Nilai V"])
    if baris:
        print(f"\nRekomendasi peringkat pertama: {baris[0].nama} (V={baris[0].v:.4f})")
