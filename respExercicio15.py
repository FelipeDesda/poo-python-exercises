from abc import ABC, abstractmethod

class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem: str): pass

class EmailService(ServicoNotificacao):
    def enviar(self, mensagem: str):
        print(f"Enviando email: {mensagem}")

class SMSService(ServicoNotificacao):
    def enviar(self, mensagem: str):
        print(f"Enviando SMS: {mensagem}")

class PushService(ServicoNotificacao):
    def enviar(self, mensagem: str):
        print(f"Enviando push: {mensagem}")

class NotificacaoService:
    def __init__(self, servico: ServicoNotificacao):
        self._servico = servico

    def notificar(self, mensagem: str):
        self._servico.enviar(mensagem)

if __name__ == "__main__":
    email = EmailService(); sms = SMSService(); push = PushService()
    n1 = NotificacaoService(email); n2 = NotificacaoService(sms); n3 = NotificacaoService(push)
    mensagem = "Bem-vindo ao sistema!"
    n1.notificar(mensagem); n2.notificar(mensagem); n3.notificar(mensagem)
