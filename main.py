# Seu primeiro programa em Python
nome = input("Digite o seu nome: ")
print(f"Olá, {nome}! Bem-vindo ao mundo do Python.")



peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

import random

numero_secreto = random.randint(1, 10)
palpite = int(input("Chute um número de 1 a 10: "))
print(f"Você {'acertou' if palpite == numero_secreto else 'errou'}. O número era {numero_secreto}!")
