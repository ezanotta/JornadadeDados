
CONSTANTE_BONUS = 1000
nome_usuario = input("Digite seu nome: ")
salario_usuario = float(input("Digite seu salario: "))
bonus_usuario= float(input("Digite o seu bonus: "))

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")

