from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self):
        self._velocidade = 0

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

    def get_velocidade(self) -> int:
        return self._velocidade

class Carro(Veiculo):
    MAX = 180
    def acelerar(self):
        self._velocidade = min(self._velocidade + 20, self.MAX)
    def frear(self):
        self._velocidade = max(self._velocidade - 20, 0)

class Bicicleta(Veiculo):
    MAX = 50
    def acelerar(self):
        self._velocidade = min(self._velocidade + 10, self.MAX)
    def frear(self):
        self._velocidade = max(self._velocidade - 10, 0)

class Aviao(Veiculo):
    MAX = 900
    def acelerar(self):
        self._velocidade = min(self._velocidade + 200, self.MAX)
    def frear(self):
        self._velocidade = max(self._velocidade - 100, 0)

class ControladorTrafego:
    def testar(self, veiculo: Veiculo):
        veiculo.acelerar()

if __name__ == "__main__":
    def testar_veiculo(veiculo: Veiculo):
        print(f"Testando {type(veiculo).__name__}")
        veiculo.acelerar()
        veiculo.acelerar()
        print(f"Velocidade: {veiculo.get_velocidade()} km/h")
        veiculo.frear()
        print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h\n")

    testar_veiculo(Carro())
    testar_veiculo(Bicicleta())
    testar_veiculo(Aviao())
