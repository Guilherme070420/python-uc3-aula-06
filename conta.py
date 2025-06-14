class contaCorrente:


    def __init__(self,nome_cliente,num_conta,senha,saldo=0.0): 
        self.nome_cliente = nome_cliente
        self.num_conta = num_conta
        #self.agencia = agencia
        self.senha = senha
        #self.cartao_credito = cartao_credito
        #self.financiamento = financiamento
        #self.cheque_especial = cheque_especial
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f"o saldo de {self.nome_cliente} disponivel é {self.saldo:.2f}")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'saque realizado com sucesso .\n Novo saldo é {self.saldo:.2f}')
        else:
            print('saldo insuficiente!')


    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f'deposito realizado com sucesso.\nNovo saldo {self.saldo:.2f}')
        else:
            print("não pode depositar valores negativos")    
        
    def transferir(self, valor, destinatario):
        if self!= destinatario.num_conta:
            contaCorrente.sacar(self, valor)
            contaCorrente.depositar(destinatario,valor)
        else:
            print('não pode realizar a transferência')




