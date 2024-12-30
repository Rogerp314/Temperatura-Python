import medidor as m
import verificador as v

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
        m.temperaturas('')
    else:
        fim = print('Muito Obrigado. Volte sempre!')
        return fim


if __name__ == '__main__':
    menu('TESTE')