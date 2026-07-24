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


idade = int(input("Digite sua idade: "))
print("Você nasceu em:", 2026 - idade)


import random

letras = "abcdefghijklmnopqrstuvwxyz1234567890!@#"
senha = "".join(random.choices(letras, k=8))
print("Sua nova senha segura é:", senha)


preco = float(input("Digite o preço do produto (R$): "))
print("Preço com 15% de desconto: R$", preco * 0.85)


import random

numeros = random.sample(range(1, 61), 6)
print("Seus números da sorte são:", sorted(numeros))


from datetime import datetime

agora = datetime.now()
print("Data e hora atual:", agora.strftime("%d/%m/%Y %H:%M:%S"))

reais = float(input("Digite o valor em Reais (R$): "))
# Simulação com o dólar médio a R$ 5,50
print(f"O valor convertido é: $ {reais / 5.50:.2f}")
