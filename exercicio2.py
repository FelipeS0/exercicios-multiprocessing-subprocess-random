#2) Fazer uma aplicação que, na main, inicialize uma variável id, inteira e inicialize 5 variáveis
#inteiras para valores, crie um vetor de parâmetros, com o id como primeiro parâmetro e um
#vetor com os 5 valores recebidos. As variáveis que recebem os valores devem receber, cada
#ma delas, um valor aleatório de 1 a 100. Esses parâmetros devem ser preenchidos para 3
#chamadas de Threads. Faça 3 chamadas de Threads, passando os parâmetros e, cada Thread,
#deve calcular a soma de cada linha (Cada iteração do laço, para a soma deve ser seguido por
#um sleep de 0.2 segundos), ao final, deve-se imprimir a identificação da linha e o resultado da
#soma.

import multiprocessing
import time
import random

def operação(id, val):
    result: int = 0
    for cont in range(5):
      result+= val[cont]
      time.sleep(0.2)
    print (f'thread {id} tem a soma igual a {result}') 
     
def main():
  id: int = 0
  val: int = 0
  param = [0]*3 
  
  for id in range (3):
     valores = [0]*5
     for cont in range(5):
      val = random.randint(1, 100)
      valores [cont]= val
     param [id] = [id, valores]
     
  with multiprocessing.Pool(processes= 3) as pool:
    pool.starmap(operação, param)    
     
if __name__ == '__main__':
  main()        