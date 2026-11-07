"""Visualisasi hasil pemeringkatan."""
def grafik_ascii(baris, lebar_maks=40):
    if not baris:
        return "Belum ada hasil untuk divisualisasikan."
    urut = sorted(baris, key=lambda item: item.v, reverse=True)
    max_v = max(item.v for item in urut) or 1.0
    panjang_nama = max(len(item.nama) for item in urut)
    garis = "-" * (panjang_nama + lebar_maks + 24)
    lines = ["", "GRAFIK PERINGKAT (nilai V)", garis]
    for item in urut:
        panjang = max(1, round(item.v / max_v * lebar_maks))
        penanda = " <- REKOMENDASI" if item.peringkat == 1 else ""
        lines.append(f"{item.peringkat}. {item.nama:<{panjang_nama}}  "
                     f"{'#' * panjang} {item.v:.4f}{penanda}")
    lines.append(garis)
    return "\n".join(lines)

def buat_grafik(baris, path_output):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return None
    if not baris:
        return None
    urut = sorted(baris, key=lambda item: item.v)
    fig, ax = plt.subplots(figsize=(9, 5))
    warna = ["#f2994a" if item.peringkat == 1 else "#17919c" for item in urut]
    bars = ax.barh([item.nama for item in urut], [item.v for item in urut], color=warna)
    for bar, item in zip(bars, urut):
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                f" {item.v:.4f}", va="center")
    ax.set_xlabel("Nilai Preferensi (V)")
    ax.set_title("Peringkat Kelayakan Penerima Bantuan UMKM (AHP-WP)")
    ax.set_xlim(0, max(item.v for item in urut) * 1.2)
    fig.tight_layout()
    fig.savefig(path_output, dpi=150)
    plt.close(fig)
    return str(path_output)
