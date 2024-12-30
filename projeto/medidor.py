#Esse arquivo tem o medidor de temperatura para saber qual está mais próxima de 0
#Coletando os dados
import verificador as v


lista_temp = list()
def temperaturas(t):
    from time import sleep
    while True:
        try:
            temp_digitado = int(input('Digite uma temperatura: '))
            if temp_digitado > 5700 or temp_digitado < -273:
                print('',end='')
            else:
                lista_temp.append(temp_digitado)
                perg = str(input('Deseja adicionar mais uma temperatura? [S/N]: ')).lower().strip()[0]
            if perg == 'n':
                print('Processando os dados',flush=True,end='')
                for i in range(0,3):
                    print('.', end='', flush=True)
                    sleep(1)
                return lista_temp
        except:
            print('\033[31m[ERROR] Digite um valor válido\033[m')



def proximo0(lista_temp):
    print()
    #Verificando qual temperatura está mais próxima de 0
    lista_distancia = list()
    for e in lista_temp:
        distancia = abs(e)
        lista_distancia.append(distancia)
    menor_temp = min(lista_distancia)
    resultado = print(f'A temperatura mais próxima de 0 registrada foi {menor_temp}')
    return resultado


if __name__ == '__main__':
    temperaturas('teste')
    proximo0(lista_temp)