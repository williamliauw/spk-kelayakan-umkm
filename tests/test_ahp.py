import unittest
import numpy as np
from spk_umkm.ahp import hitung_ahp, matriks_ahp_default, validasi_matriks

class TestAHP(unittest.TestCase):
    def test_bobot_berjumlah_satu(self):
        hasil = hitung_ahp(matriks_ahp_default())
        self.assertAlmostEqual(float(hasil.bobot.sum()), 1.0, places=7)

    def test_matriks_default_resiprokal(self):
        hasil = hitung_ahp(matriks_ahp_default())
        self.assertEqual(hasil.bobot.shape[0], 5)

    def test_matriks_tidak_persegi_ditolak(self):
        with self.assertRaises(ValueError):
            validasi_matriks(np.array([[1, 2, 3], [0.5, 1, 2]]))

    def test_matriks_nilai_nol_ditolak(self):
        with self.assertRaises(ValueError):
            validasi_matriks(np.array([[1, 0], [1, 1]]))

    def test_matriks_tidak_resiprokal_ditolak(self):
        with self.assertRaises(ValueError):
            validasi_matriks(np.array([[1, 2], [0.4, 1]]))

if __name__ == "__main__":
    unittest.main()
