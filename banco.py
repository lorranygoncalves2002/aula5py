class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def consultar(self):
        print('titular:', self.titular)
        print('saldo:', self.saldo)
        print("-" *20)

    def depositar(self, valor):
        # valor = float(input('Informe o valor:'))
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        # valor = float(input('Informe o valor do saque:'))
        if valor <= self.saldo:
          self.saldo = self.saldo - valor
        else:
            print('transação não aceita!!!!!!')

    def transferir(self, destinatario, valor):
        if valor >0 and valor< self.saldo:
           self.saldo = self.saldo - valor
           destinatario.depositar(valor)


c1 = Conta('maria', 1000)
c2 = Conta('joao',  500)
c1.transferir(c2, 500)
c1.consultar()
c2.consultar()


