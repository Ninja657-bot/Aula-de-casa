import os 
import time
os.system("cls")

name = input("Por favor digite seu nome: ")
for i in range(3):
    print("\r" + "." * (i+1), end="")
    time.sleep(1)
print(f"\nSeu nome é {name}")
