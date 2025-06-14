from conta import contaCorrente

contas =  {
    '321': contaCorrente ('guilherme','321', 'guizim123',1000.0),
    '456': contaCorrente('giovanny','456','giovanny456',2000.0) 
}

# login

contaCorrente.mostrar_saldo(contas['321'])