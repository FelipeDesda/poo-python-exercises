from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperatura, umidade, pressao): pass

class EstacaoMeteorologica:
    def __init__(self):
        self._observers = []
        self._temperatura = None
        self._umidade = None
        self._pressao = None

    def adicionar_observer(self, obs: Observer):
        self._observers.append(obs)

    def remover_observer(self, obs: Observer):
        self._observers.remove(obs)

    def notificar_observers(self):
        for obs in self._observers:
            obs.update(self._temperatura, self._umidade, self._pressao)

    def definir_medicoes(self, temperatura, umidade, pressao):
        self._temperatura = temperatura
        self._umidade = umidade
        self._pressao = pressao
        self.notificar_observers()

class DisplayTemperatura(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Temperatura: {temperatura}°C")

class DisplayUmidade(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Umidade: {umidade}%")

class DisplayCompleto(Observer):
    def update(self, temperatura, umidade, pressao):
        print(f"Display Completo: {temperatura}°C, {umidade}%, {pressao} hPa")

if __name__ == "__main__":
    estacao = EstacaoMeteorologica()

    display_temp = DisplayTemperatura()
    display_umidade = DisplayUmidade()
    display_completo = DisplayCompleto()

    estacao.adicionar_observer(display_temp)
    estacao.adicionar_observer(display_umidade)
    estacao.adicionar_observer(display_completo)

    estacao.definir_medicoes(25.5, 65.0, 1013.2)
    estacao.definir_medicoes(27.0, 70.0, 1015.1)
