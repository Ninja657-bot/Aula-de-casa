import os
os.system("cls")

soma = (0)

for i in range(3):
    nota = float(input("Digite sua nota: "))
    soma += nota
media = float(soma / 3)
print(f"A soma das sua notas é: {soma}")
print(f"Sua média foi: {media}")
if media >= 7:
    print("Você foi aprovado")
if media >= 4 <= 6.9:
    print("Você está de recuperação")
if media < 4:
    print("Você foi reprovado")