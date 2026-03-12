import os 
os.system("cls")

soma = float(0.0)

for i in range(4):
    notas = float(input("Digite sua nota: "))
    print(f"{soma} + {notas} = {soma + notas}")
    soma += notas

media = soma / 4
print(f"{soma} / 4 = {media}")
print(f"A média das suas notas é: {media}")