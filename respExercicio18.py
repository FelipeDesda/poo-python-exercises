class Amplificador:
    def ligar(self): print("Ligando amplificador")
    def definir_volume(self, volume): print(f"Definindo volume para {volume}")

class DVDPlayer:
    def ligar(self): print("Ligando DVD player")
    def reproduzir(self, filme): print(f"Reproduzindo {filme}")

class Projetor:
    def ligar(self): print("Ligando projetor")
    def modo_widescreen(self): print("Definindo modo widescreen")

class Luzes:
    def diminuir(self, nivel): print(f"Diminuindo luzes para {nivel}%")

class PipocaPopper:
    def ligar(self): print("Ligando pipoqueira")
    def fazer_pipoca(self): print("Fazendo pipoca")

class HomeTheaterFacade:
    def __init__(self):
        self.amp = Amplificador()
        self.dvd = DVDPlayer()
        self.proj = Projetor()
        self.luzes = Luzes()
        self.pipoca = PipocaPopper()

    def assistir_filme(self, filme):
        print(f"Preparando para assistir {filme}...")
        self.amp.ligar()
        self.amp.definir_volume(5)
        self.dvd.ligar()
        self.proj.ligar()
        self.proj.modo_widescreen()
        self.luzes.diminuir(10)
        self.pipoca.ligar()
        self.pipoca.fazer_pipoca()
        self.dvd.reproduzir(filme)

    def fim_filme(self):
        print("Filme finalizado! Desligando tudo...")
        # Simulação simples de desligar
        print("Desligando amplificador, DVD, projetor e retornando luzes ao normal.")

if __name__ == "__main__":
    ht = HomeTheaterFacade()
    ht.assistir_filme("Matrix")
    ht.fim_filme()
