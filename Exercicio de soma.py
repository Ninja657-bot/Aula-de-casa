import os 
import time
os.system("cls")

soma = 0

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    time.sleep(1)
    print(soma, "+", numero, "=", soma + numero)
    soma =+ numero


print("Resultado final:", soma)

    
