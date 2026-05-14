#3) Fazer uma aplicação de uma corrida de sapos, com 5 Threads, cada Thread controlando 1
#sapo. Deve haver um tamanho máximo para cada pulo do sapo (em centímetros) e a distância
#máxima para que os sapos percorram. A cada salto, um sapo pode dar um salto de 0 até o
#tamanho máximo do salto (valor aleatório entre 1 e 5 cm.). Após dar um salto, a Thread, para
#cada sapo, deve mostrar no console, qual foi o tamanho do salto e quanto o sapo percorreu.
#Assim que o sapo percorrer a distância máxima, a Thread deve apresentar que o sapo chegou.
#Dica: O exercício deve ser resolvido todo em console, ou seja, como se estivesse sendo narrado.
import multiprocessing
import random

def corrida(id_sapo):
 pulo: int = 0
 dist_perc: int = 0
 val: int = 0
 while dist_perc < 100: 
     val = random.randint(1, 5)
     pulo = val
     dist_perc+= pulo
     print(f'O sapo {id_sapo} andou {pulo} e percorreu {dist_perc}!')
     if dist_perc >= 100:
      print (f'O sapo {id_sapo} chegou na linha final!!')
      break
 
def main():
    param: int = [0]*5
    for cont in range(5):
     param [cont]= cont + 1
     
    with multiprocessing.Pool(processes= 5) as pool:
        pool.map(corrida, param)
    
        
if __name__ == '__main__':
    main()        
    