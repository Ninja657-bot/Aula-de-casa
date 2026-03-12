import os 
import time
os.system("cls")
 
numero = int(input("Digite um número: "))
for i in range (1 ,11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")    