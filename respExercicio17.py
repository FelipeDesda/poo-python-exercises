from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def get_descricao(self) -> str: pass
    @abstractmethod
    def get_preco(self) -> float: pass

class Cafe(Bebida):
    def get_descricao(self): return "Café"
    def get_preco(self): return 5.0

class Cha(Bebida):
    def get_descricao(self): return "Chá"
    def get_preco(self): return 3.0

class BebidaDecorator(Bebida):
    def __init__(self, bebida: Bebida):
        self.bebida = bebida

class LeiteDecorator(BebidaDecorator):
    def get_descricao(self): return f"{self.bebida.get_descricao()} com Leite"
    def get_preco(self): return self.bebida.get_preco() + 2.0

class AcucarDecorator(BebidaDecorator):
    def get_descricao(self): return f"{self.bebida.get_descricao()} com Açúcar"
    def get_preco(self): return self.bebida.get_preco() + 0.5

class ChantillyDecorator(BebidaDecorator):
    def get_descricao(self): return f"{self.bebida.get_descricao()} com Chantilly"
    def get_preco(self): return self.bebida.get_preco() + 3.0

if __name__ == "__main__":
    cafe = Cafe()
    print(f"{cafe.get_descricao()} - R$ {cafe.get_preco():.2f}")

    cafe_com_leite = LeiteDecorator(cafe)
    print(f"{cafe_com_leite.get_descricao()} - R$ {cafe_com_leite.get_preco():.2f}")

    cafe_especial = ChantillyDecorator(AcucarDecorator(LeiteDecorator(Cafe())))
    print(f"{cafe_especial.get_descricao()} - R$ {cafe_especial.get_preco():.2f}")
