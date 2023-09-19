import random 

  
# Use uma variável para armazenar a resposta para continuar jogando o dado
response = "y"
   
while response == "y": 
      
    # Gere um número aleatório 
    # entre 1 e 6 (incluindo 
    # os números 1 e 6) 
    no = random.randint(1,6) 

    # condições para verificar o valor numérico  
    if no == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]") 
    if no == 2: 
        print("[-----]") 
        print("[ 0   ]") 
        print("[     ]") 
        print("[   0 ]") 
        print("[-----]") 
    if no == 3: 
        print("[-----]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[-----]") 
    if no == 4: 
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 5: 
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 6: 
        print("[-----]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[-----]") 
          
    # Peça para o usuário informar uma resposta      
    response=input("Pressione y para jogar novamente e n para sair:") 
    print("\n") 


import time
from playsound import playsound


# defina a função de contagem regressiva do cronômetro
def countdown_timer(seconds):
    while seconds > 0:

        mins = int(seconds / 60)
        secs = int(seconds % 60)
        
        timer = f'{mins}:{secs}'
        
        print(timer,end='\r')
        time.sleep(1)
        seconds -= 1
    
    print('Tempo Esgotado!')
    playsound('mixkit-sound.wav')


# digite o tempo em segundos
seconds = input("Digite o tempo em segundos: ")
# chamada da função
countdown_timer(int(seconds))