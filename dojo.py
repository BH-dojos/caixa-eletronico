class CaixaEletronico():

    def obter_menor_numero_de_notas(self, valor):
        saldo = valor
        resultado = []
        while saldo > 0:
            nota_atual = self._maior_nota_que_cabe_no(saldo)
            saldo -= nota_atual
            resultado.append(nota_atual)


        return resultado


    def _maior_nota_que_cabe_no(self, saldo):
        if saldo >= 100:
            return 100
        elif saldo >= 50:
            return 50
        elif saldo >= 20:
            return 20
        elif saldo >=10:
            return 10
        else:
            raise DojoExcecao

class DojoExcecao(Exception):
    pass