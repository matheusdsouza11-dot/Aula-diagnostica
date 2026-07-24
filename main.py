# Seu primeiro programa em Python
nome = input("Digite o seu nome: ")
print(f"Olá, {nome}! Bem-vindo ao mundo do Python.")



peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")