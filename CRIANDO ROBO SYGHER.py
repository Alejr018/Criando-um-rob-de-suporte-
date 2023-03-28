from time import sleep
nome = str(input('Digite seu primeiro nome:')).capitalize()
print('---------------------------------------------------------------------------------')
nome2 = str(input('Digite seu sobrenome:')).capitalize()
print('''Olá,{} {},seja bem vindo aos suportes Sygher,seu sou o assistente virtual WolfBot
e estou aqui para te ajudar'''.format(nome, nome2))
escolha = 0
while escolha!=100:
    print('''------------------------------------------------------------------
Escolha uma da opções abaixo para prosseguir
[1] Ofertas do momento
[2] Formas de pagamento 
[3] Fale Conosco ''')
    escolha = int(input(''))
    if escolha == 1:
        print('''As ofertas do momento são:
    Mouse pad:SyGaming R$:80.00
    Camiseta Drop:Basic R$45:00 e dus por R$:80.00'''.replace(".",(',')))
        escolha = str(input('Deseja adquirir ?'))
        if escolha == 'sim':
            print('Ok,vamos te encaminhar para o link de ofertas')
        else:
            print('Ok')
    elif escolha == 2:
        print('''As formas de pagamentos são 
        Pix
        Transferência Bancária 
        Boleto 
        Cartão Parcelado em 5X com juros''')
    elif escolha == 3:
        print('Vamos de encaminhar para um chat em tempo real com um de nossos atendente \n guarde...')
        for contagem in range(0, 11):
            sleep(0.80)
            print(contagem)
    else:
        print('Opção Inválida,tente alguma das opções acima')






