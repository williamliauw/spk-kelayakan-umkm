# Metodologi AHP dan Weighted Product

## 1. Analytical Hierarchy Process (AHP)

AHP digunakan untuk memperoleh bobot prioritas setiap kriteria melalui matriks
perbandingan berpasangan. Program menormalisasi setiap kolom, lalu menghitung
rata-rata setiap baris sebagai bobot prioritas.

Program menghitung:
- Lambda maksimum (lambda max)
- Consistency Index (CI)
- Random Index (RI)
- Consistency Ratio (CR)

Matriks dinyatakan konsisten apabila CR <= 0,10.

## 2. Weighted Product (WP)

WP menggunakan bobot AHP untuk menghitung nilai preferensi setiap alternatif:

S_i = hasil perkalian skor kriteria berpangkat bobotnya.

V_i = S_i / jumlah seluruh S.

Alternatif diurutkan berdasarkan nilai V dari terbesar ke terkecil.

## 3. Perlakuan kriteria jarak

Kriteria C5 secara konsep merupakan cost. Namun pemetaan sub-kriteria sudah
membalik skor sehingga jarak yang lebih dekat memperoleh skor lebih tinggi.
Oleh karena itu, seluruh skor diperlakukan sebagai benefit pada perhitungan WP.
Jangan membalik arah C5 sekali lagi tanpa mengubah pemetaan skornya.
