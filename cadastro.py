nome = input("Insira seu nome: ")
while len(nome) <= 3:
    nome = input("Seu nome deve ter mais de 3 letras. Insira novamente: ")

idade = int(input("Insira sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Sua idade deve estar entre 0 e 150. Insira novamente: "))

salario = float(input("Insira seu salário: "))
while salario <= 0:
    salario = float(input("Seu salário deve ser maior que zero. Insira novamente: "))

genero = input("Insira seu gênero (m/f): ")
while genero not in ["M", "F"]:
    genero = input("Seu gênero deve ser 'm' ou 'f'. Insira novamente: ")

estado_civil = input("Insira seu estado civil (S/C/V/D): ")
while estado_civil not in ["S", "C", "V", "D"]:
    estado_civil = input("Seu estado civil deve ser 'S', 'C', 'V' ou 'D'. Insira novamente: ")

print("Resumo dos dados informados:")
print("Nome: ", nome)
print("Idade: ", idade)
print("Salário: R$", salario)
print("Gênero: ", genero)
print("Estado civil: ", estado_civil)
 