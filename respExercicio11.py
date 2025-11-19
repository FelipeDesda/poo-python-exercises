class Funcionario:
    def __init__(self, nome: str, salario: float, cargo: str):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

class CalculadoraSalario:
    def calcular_salario_liquido(self, funcionario: Funcionario, descontos: float) -> float:
        return funcionario.salario - descontos

class GeradorRelatorio:
    def gerar_relatorio(self, funcionario: Funcionario) -> str:
        return f"Relatório: {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario:.2f}"

class RepositorioFuncionario:
    def __init__(self):
        self._banco_simulado = []

    def salvar(self, funcionario: Funcionario):
        # Simula persistência
        self._banco_simulado.append({'nome': funcionario.nome, 'salario': funcionario.salario, 'cargo': funcionario.cargo})
        print(f"Salvo: {funcionario.nome}")

if __name__ == "__main__":
    funcionario = Funcionario("Ana Silva", 5000.0, "Desenvolvedora")
    calculadora = CalculadoraSalario()
    gerador = GeradorRelatorio()
    repositorio = RepositorioFuncionario()

    salario_liquido = calculadora.calcular_salario_liquido(funcionario, 500.0)
    relatorio = gerador.gerar_relatorio(funcionario)
    repositorio.salvar(funcionario)

    print(f"Salário líquido: R$ {salario_liquido:.2f}")
    print(relatorio)
