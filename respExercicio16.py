class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        raise NotImplementedError

class ProcessadorPagamentoInterno(ProcessadorPagamento):
    def processar_pagamento(self, valor, cartao):
        return f"Interno: Processando R$ {valor} no cartão {cartao}"

class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando R$ {amount} no cartão {credit_card_number}"

class PayPalAdapter(ProcessadorPagamento):
    def __init__(self, paypal_api: PayPalAPI):
        self.paypal = paypal_api
    def processar_pagamento(self, valor, cartao):
        # adapta nomes/ordens para a API do PayPal
        return self.paypal.make_payment(valor, cartao)

class SistemaPagamento:
    def __init__(self, processor: ProcessadorPagamento):
        self.processor = processor
    def realizar_pagamento(self, valor, cartao):
        resultado = self.processor.processar_pagamento(valor, cartao)
        print(resultado)

if __name__ == "__main__":
    interno = ProcessadorPagamentoInterno()
    sistema1 = SistemaPagamento(interno)
    paypal_api = PayPalAPI()
    paypal_adapter = PayPalAdapter(paypal_api)
    sistema2 = SistemaPagamento(paypal_adapter)

    sistema1.realizar_pagamento(100.0, "1234-5678")
    sistema2.realizar_pagamento(200.0, "8765-4321")
