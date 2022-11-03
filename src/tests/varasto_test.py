import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_liikaa(self):
        self.varasto.lisaa_varastoon(9999)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_otetaan_enemman_kun_max(self):
        self.varasto.ota_varastosta(9999)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_ota_nolla(self):
        self.varasto.lisaa_varastoon(2)
        self.varasto.ota_varastosta(0)
        self.assertAlmostEqual(self.varasto.saldo, 2)
    
    def test_otetaan_enemman_kun_max_pre(self):
        self.varasto.lisaa_varastoon(22)
        self.varasto.ota_varastosta(9999)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_lisaa_nolla(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_varasto_neg_koko(self):
        v = Varasto(-5)
        self.assertAlmostEqual(v.tilavuus, 0)
    
    def test_varasto_alkusaldo_isompi_kun_max(self):
        v = Varasto(5, alku_saldo=6)
        self.assertAlmostEqual(v.saldo, 5)
    
    def test_varasto_alkusaldo_neg(self):
        v = Varasto(5, alku_saldo=-5)
        self.assertAlmostEqual(v.saldo, 0)

    def test_varasto_alkusaldo_ja_max_neg(self):
        v = Varasto(-5, alku_saldo=-5)
        self.assertAlmostEqual((v.saldo, v.tilavuus), (0, 0))

    def test_str(self):
        self.assertAlmostEqual(str(self.varasto), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")
    
    def test_lisaa_neg(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_ota_neg(self):
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
