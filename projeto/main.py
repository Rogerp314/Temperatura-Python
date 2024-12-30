#Programa Principal
import verificador as v
from menu import *

arq = 'dados.txt'

if not v.arquivoExiste(arq):
    v.Criar(arq)

menu('MEDIDOR DE TEMPERATURA')