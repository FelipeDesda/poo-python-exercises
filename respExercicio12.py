from abc import ABC, abstractmethod

class CalculadorDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class DescontoEstudante(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.90

class DescontoFuncionario(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.85

class DescontoVIP(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.80

class ProcessadorPagamento:
    def processar(self, valor: float, calculador: CalculadorDesconto) -> float:
        return calculador.calcular(valor)

# Exemplo de extensão sem modificar código existente:
class DescontoBlackFriday(CalculadorDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.70

if __name__ == "__main__":
    pagamento = ProcessadorPagamento()
    valor_original = 1000.0

    desconto_estudante = DescontoEstudante()
    desconto_funcionario = DescontoFuncionario()
    desconto_vip = DescontoVIP()
    desconto_bf = DescontoBlackFriday()

    print(f"Estudante: R$ {pagamento.processar(valor_original, desconto_estudante):.2f}")
    print(f"Funcionário: R$ {pagamento.processar(valor_original, desconto_funcionario):.2f}")
    print(f"VIP: R$ {pagamento.processar(valor_original, desconto_vip):.2f}")
    print(f"Black Friday (nova extensão): R$ {pagamento.processar(valor_original, desconto_bf):.2f}")
