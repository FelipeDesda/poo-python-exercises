from abc import ABC, abstractmethod

class Trabalhavel(ABC):
    @abstractmethod
    def trabalhar(self): pass

class Alimentavel(ABC):
    @abstractmethod
    def comer(self): pass

class Descansavel(ABC):
    @abstractmethod
    def dormir(self): pass

class Programavel(ABC):
    @abstractmethod
    def programar(self): pass

class Desenvolvedor(Trabalhavel, Alimentavel, Descansavel, Programavel):
    def __init__(self, nome): self.nome = nome
    def trabalhar(self): print(f"{self.nome} está trabalhando.")
    def comer(self): print(f"{self.nome} está comendo.")
    def dormir(self): print(f"{self.nome} está dormindo.")
    def programar(self): print(f"{self.nome} está programando.")

class Gerente(Trabalhavel, Alimentavel, Descansavel):
    def __init__(self, nome): self.nome = nome
    def trabalhar(self): print(f"{self.nome} (Gerente) está trabalhando.")
    def comer(self): print(f"{self.nome} (Gerente) está comendo.")
    def dormir(self): print(f"{self.nome} (Gerente) está dormindo.")

class Robo(Trabalhavel, Programavel):
    def __init__(self, id): self.id = id
    def trabalhar(self): print(f"Robô {self.id} está executando tarefa.")
    def programar(self): print(f"Robô {self.id} está sendo programado.")

if __name__ == "__main__":
    dev = Desenvolvedor("Ana")
    ger = Gerente("Carlos")
    robo = Robo("R2D2")

    dev.trabalhar(); dev.comer(); dev.programar()
    print()
    ger.trabalhar(); ger.comer()
    print()
    robo.trabalhar(); robo.programar()
