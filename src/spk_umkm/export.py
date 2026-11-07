"""Ekspor data dan hasil analisis ke Excel atau CSV."""
from pathlib import Path
import pandas as pd
from .criteria import KRITERIA, KODE_KRITERIA, NAMA_KRITERIA

def ekspor_hasil(alternatif, hasil_ahp, hasil_wp, path_output):
    path = Path(path_output)
    path.parent.mkdir(parents=True, exist_ok=True)

    df_alt = pd.DataFrame([
        {"Nama UMKM": alt.nama,
         **{k.nama: alt.nilai[k.kode] for k in KRITERIA}}
        for alt in alternatif
    ])
    df_bobot = pd.DataFrame({
        "Kode": KODE_KRITERIA, "Kriteria": NAMA_KRITERIA,
        "Bobot": hasil_ahp.bobot,
        "Persentase": [f"{b*100:.2f}%" for b in hasil_ahp.bobot],
    })
    df_konsistensi = pd.DataFrame({
        "Parameter": ["Lambda Max", "CI", "RI", "CR", "Status"],
        "Nilai": [hasil_ahp.lambda_max, hasil_ahp.ci, hasil_ahp.ri,
                  hasil_ahp.cr, "Konsisten" if hasil_ahp.konsisten else "Tidak Konsisten"],
    })
    df_wp = pd.DataFrame([
        {"Peringkat": item.peringkat, "Nama UMKM": item.nama,
         **{kode: item.skor[kode] for kode in KODE_KRITERIA},
         "Nilai S": item.s, "Nilai V": item.v}
        for item in hasil_wp
    ])

    if path.suffix.lower() == ".csv":
        path.mkdir(parents=True, exist_ok=True)
        df_alt.to_csv(path / "data_alternatif.csv", index=False)
        df_bobot.to_csv(path / "bobot_ahp.csv", index=False)
        df_konsistensi.to_csv(path / "uji_konsistensi_ahp.csv", index=False)
        df_wp.to_csv(path / "hasil_wp_ranking.csv", index=False)
        return str(path.resolve())

    try:
        with pd.ExcelWriter(path, engine="openpyxl") as writer:
            df_alt.to_excel(writer, sheet_name="Data Alternatif", index=False)
            df_bobot.to_excel(writer, sheet_name="Bobot AHP", index=False)
            df_konsistensi.to_excel(writer, sheet_name="Uji Konsistensi", index=False)
            df_wp.to_excel(writer, sheet_name="Hasil WP", index=False)
        return str(path.resolve())
    except ImportError:
        folder = path.with_suffix("")
        folder.mkdir(parents=True, exist_ok=True)
        df_alt.to_csv(folder / "data_alternatif.csv", index=False)
        df_bobot.to_csv(folder / "bobot_ahp.csv", index=False)
        df_konsistensi.to_csv(folder / "uji_konsistensi_ahp.csv", index=False)
        df_wp.to_csv(folder / "hasil_wp_ranking.csv", index=False)
        return str(folder.resolve())
