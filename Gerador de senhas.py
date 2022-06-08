import random

print("Seja bem vindo, Em breve vamos gerar sua senha")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%*(),.0123456789"
number = input ('Quantidade de senhas para gerar:')
number = int(number)
length = input('Input yout password lengt')
length = int(length)
print("\nhere are you passwords: ")
for pwd in range (number):
  passwords = " "
for c in range (length):
  passwords += random.choice(chars)
  print(passwords)