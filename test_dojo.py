import unittest
import dojo

class TestDojo(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_notas_para_100_eh_uma_de_100(self):
        self.assertEqual(dojo.obter_menor_numero_de_notas(100), [100])

    def test_notas_para_50_eh_uma_de_50(self):
        self.assertEqual(dojo.obter_menor_numero_de_notas(50), [50])

    def test_notas_para_20_eh_uma_de_20(self):
        self.assertEqual(dojo.obter_menor_numero_de_notas(20), [20])

    def test_notas_para_10_eh_uma_de_10(self):
        self.assertEqual(dojo.obter_menor_numero_de_notas(10), [10])

    def test_notas_para_30_sao_uma_de_10_e_uma_de_20(self):
        self.assertEqual(dojo.obter_menor_numero_de_notas(30), [20, 10])

    def test_notas_para_120_sao_uma_de_100_e_uma_de_20(self):
        self.assertEqual(dojo.obter_menor_numero_de_notas(120), [100, 20])

    def test_notas_para_500_sao_cinco_de_100(self):
        self.assertEqual(dojo.obter_menor_numero_de_notas(500), [100, 100, 100, 100, 100])

    def test_notas_para_130_sao_uma_100_uma_20_e_uma_10(self):
        self.assertEqual(dojo.obter_menor_numero_de_notas(130), [100, 20, 10])

    def test_notas_para_9_levanta_excecao_nao_permite_sacar(self):
        self.assertRaises(dojo.DojoExcecao, dojo.obter_menor_numero_de_notas, 9)

    def test_notas_para_180_sao_uma_100_uma_50_uma_20_e_uma_10(self):
        self.assertEqual(dojo.obter_menor_numero_de_notas(180), [100,50, 20, 10])


if __name__ == 'main':
    unittest.main()