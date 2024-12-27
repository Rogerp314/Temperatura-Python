#Programa Principal
import verificador as v
import medidor as m

cu =list()
def menu(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)
    print('''=>Inserir temperaturas menualmente [1]
=>Ultilizar arquivo de texto [2]
=>Sair [3]''')
    print('-'*40)
    res = v.resposta('Sua opção: ')
    if res == 1:
        temp = m.temperaturas('')
        m.proximo0(temp)
    elif res == 2:
        pass
    else:
        fim = print('Muito Obrigado. Volte sempre!')
        return fim


menu('MEDIDOR DE TEMPERATURA')