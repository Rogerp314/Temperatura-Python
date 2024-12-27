#Esse arquivo serve para tratamento de erros e verificação do arquivo txt

#Verificador de resposta
def resposta(res):
    while True:
        try:
            res = int(input('Sua opção: '))
            if res < 1 or res > 3:
                print('\033[31m[ERROR] Digite uma opção válida\033[m')
            else:
                return res
        except:
            print('\033[31m[ERROR] Digite uma opção válida\033[m')




#Área de testes
if __name__ == '__main__':
    resposta('teste')