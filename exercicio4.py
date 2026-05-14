# 4) No Sistema Operacional Linux, o comando para realizar uma operação de ping com 10
#iterações é ping -4 -c 10 <servidor> e no Sistema Operacional Windows, o comando para a
#mesma função é ping -4 -n 10 <servidor>. Fazer uma aplicação Java que rode 3 Threads, sendo
#que a Thread deve identificar o SO para rodar o comando certo, fazendo operação de ping para
#os servidores UOL (www.uol.com.br), Terra (www.terra.com.br) e Google (www.google.com.br).
#Cada thread deve ler a saída do ping imprimindo, a cada iteração, o nome do servidor (usar
#fixo: UOL, Terra ou Google) e o tempo daquela iteração. Ao fim, deve-se exibir o nome do
#servidor (usar fixo: UOL, Terra ou Google) e o tempo médio obtido pela operação. Outros
#Sistemas Operacionais devem ser descartados.
import multiprocessing
import platform
import subprocess

def Os():
    return platform.system()

def ping(servidor):
    system: str = ''
    processo: str = []
    saida: str = ''
    linha: str = ''
    nome: str = ''
    parte: str = []
    num: str = []
    c: int = 0
    
    system = Os()
    if system == 'Windows':
        processo = ['ping', '-4', '-n', '10', servidor]
        
    elif system == 'Linux':
        
        processo = ['ping', '-4', '-c' , '10', servidor] 
    else:
        print ('Sistema Inválido!')
        return   
    
    if 'uol' in servidor:
        nome = 'UOL' 
    elif 'google' in servidor:
        nome = 'Google' 
    else:
        nome = 'Terra'              
    saida = subprocess.Popen(processo, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors= 'ignore')
    
    while (linha != ''):
        linha = saida.stdout.readline().decode('utf-8', errors= 'ignore')
        
        if 'time' in linha:
            parte = linha.split('time=')
            if len(parte) > 1:
             num = parte[1].split(' ')[0]
             print (nome, 'time=', num)
        if 'Average' in linha:
            parte = linha.replace('\r', '').replace('\n', '').split(' ')
            for c in range(0, len(parte)):
                if parte[c] == 'Average':
                    print (nome, parte[c], parte [c+1], parte[c+2])
        if 'avg' in linha:
            
            parte = linha.replace('\r', '').replace('\n', '').split('/')
            for c in range (0, len(parte)):
                if parte[c] == 'avg':
                    print (nome, parte[c],"=", parte[c+3], "ms")   
        
def main():
    vet: str = ['www.uol.com.br', 'www.terra.com.br', 'www.google.com.br' ]
    id: int = 0
    param: str = ['']*3
    
    for id in range(3):
        param[id] = vet[id]
        
    with multiprocessing.Pool(processes= 3) as pool:
            pool.map(ping, param)
        
           
        
            

if __name__ == '__main__':
    main()