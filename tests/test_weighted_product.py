import unittest
from spk_umkm.sample_data import data_contoh
from spk_umkm.ahp import hitung_ahp, matriks_ahp_default
from spk_umkm.weighted_product import hitung_wp

class TestWeightedProduct(unittest.TestCase):
    def setUp(self):
        self.alternatif = data_contoh()
        self.bobot = hitung_ahp(matriks_ahp_default()).bobot

    def test_total_nilai_preferensi_satu(self):
        hasil = hitung_wp(self.alternatif, self.bobot)
        self.assertAlmostEqual(sum(item.v for item in hasil), 1.0, places=7)

    def test_peringkat_berurutan(self):
        hasil = hitung_wp(self.alternatif, self.bobot)
        self.assertEqual([item.peringkat for item in hasil],
                         list(range(1, len(hasil) + 1)))
        self.assertEqual(hasil, sorted(hasil, key=lambda item: item.v, reverse=True))

    def test_data_kosong_ditolak(self):
        with self.assertRaises(ValueError):
            hitung_wp([], self.bobot)

if __name__ == "__main__":
    unittest.main()
