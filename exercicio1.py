import multiprocessing
import time

#1) Fazer uma aplicação que rode 5 Threads que cada uma delas receba um inteiro chamado id
#como parâmetro e imprima no console o texto “Thread #” + id. Antes de imprimir o valor, deve-
#se fazer um sleep de 0.5 segundos.

def operação(id):
    time.sleep(0.5)
    print (f'Thread #{id}')
    


def main():
    p: int = 0
    param = [0]*5
    for p in range(5):
        param[p] = p + 1
    with multiprocessing.Pool(processes= p) as pool:
            pool.map(operação, param)

if __name__ == '__main__':
  main()        