"""Titik masuk aplikasi SPK UMKM."""
import argparse
from pathlib import Path
from spk_umkm.sample_data import data_contoh
from spk_umkm.ahp import hitung_ahp, matriks_ahp_default
from spk_umkm.weighted_product import hitung_wp
from spk_umkm.reporting import laporan_ahp, laporan_wp
from spk_umkm.visualization import grafik_ascii, buat_grafik
from spk_umkm.export import ekspor_hasil
from spk_umkm.app import AplikasiSPK

def jalankan_demo():
    alternatif = data_contoh()
    hasil_ahp = hitung_ahp(matriks_ahp_default())
    hasil_wp = hitung_wp(alternatif, hasil_ahp.bobot)
    laporan_ahp(hasil_ahp)
    laporan_wp(hasil_wp, hasil_ahp.bobot)
    print(grafik_ascii(hasil_wp))
    Path("outputs").mkdir(exist_ok=True)
    grafik = buat_grafik(hasil_wp, Path("outputs/hasil_peringkat.png"))
    ekspor = ekspor_hasil(alternatif, hasil_ahp, hasil_wp,
                          "outputs/hasil_spk_umkm.xlsx")
    print("\nFile keluaran:")
    print(f"- Grafik: {grafik or 'Matplotlib tidak tersedia'}")
    print(f"- Laporan: {ekspor}")

def main():
    parser = argparse.ArgumentParser(
        description="SPK kelayakan penerima bantuan UMKM dengan AHP dan WP")
    parser.add_argument("--demo", action="store_true",
                        help="jalankan simulasi dengan data contoh")
    args = parser.parse_args()
    if args.demo:
        jalankan_demo()
    else:
        AplikasiSPK().menu()

if __name__ == "__main__":
    main()
