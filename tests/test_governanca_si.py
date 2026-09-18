import unittest

from src.governanca_si import calcular_eficiencia_financeira


class TestEficienciaFinanceira(unittest.TestCase):
    def test_alerta_para_volume_abaixo_de_15_m3(self):
        resultado = calcular_eficiencia_financeira(14.9)

        self.assertEqual(resultado, "Alerta: Alto Custo de Ociosidade Detectado")

    def test_aceita_volume_exatamente_no_limite(self):
        resultado = calcular_eficiencia_financeira(15.0)

        self.assertEqual(resultado, "Eficiencia Economica Aceitavel")

    def test_rejeita_volume_fora_da_capacidade_da_frota(self):
        for volume in (-0.1, 50.1):
            with self.subTest(volume=volume):
                resultado = calcular_eficiencia_financeira(volume)

                self.assertEqual(resultado, "Erro: Volume Invalido")

    def test_rejeita_entrada_nao_numerica(self):
        try:
            resultado = calcular_eficiencia_financeira("dez")
        except TypeError:
            resultado = None

        self.assertEqual(resultado, "Erro: Volume Invalido")


if __name__ == "__main__":
    unittest.main()
