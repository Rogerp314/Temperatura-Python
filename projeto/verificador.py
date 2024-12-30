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


#Verificando se o arquivo de dados existe:
def arquivoExiste(nome): #Retorna True ou False para a existencia do arquivo
    try:
        abrir = open(nome, 'rt')
        abrir.close()
    except:
        return False
    else:
        return True


#Criando o arquivo caso não exista
def Criar(nome):
    try:
        arquivo = open(nome, 'wt+')
    except:
        print()


#Lendo o arquivo
def ler(nome):
    pass


#Verificar se vai usar o arquivo de texto para o medidor
def arqDados(resposta):
    if resposta == 2:
        return True
    else:
        return False    



#Área de testes
if __name__ == '__main__':
    resposta('teste')
    print(arquivoExiste('teste'))