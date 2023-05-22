
class NumeroPerfeito:
    @staticmethod
    def verificador(valor_para_teste):
        soma_divisores = 0
        for i in range(1, valor_para_teste):
            if valor_para_teste % i == 0:
                soma_divisores += i

        if soma_divisores == valor_para_teste:
            return f"{valor_para_teste} eh perfeito"

        else:
            return f"{valor_para_teste} não eh perfeito"
