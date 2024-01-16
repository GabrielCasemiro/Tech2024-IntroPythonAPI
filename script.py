# Imprime "Hello world"
print("Hello world")

# Variáveis e tipos de dados
mensagem = "Hello world"  # Texto
print(mensagem)

numero_inteiro = 42  # int
numero_decimal = 42.5  # float
print("numero_decimal:", numero_decimal)
print("tipo da variavel numero_decimal:", type(numero_decimal))
print("numero_inteiro:", numero_inteiro)
print("tipo da variavel numero_inteiro:", type(numero_inteiro))

booleano = True
print("booleano:", booleano)
print("tipo da variavel booleano:", type(booleano))

# Listas
lista = [1, numero_decimal, 3, numero_inteiro, booleano]
print("lista:", lista)
print("lista[0]:", lista[0])
print("lista[1]:", lista[1])
print("lista[2]:", lista[2])
print("tamanho da lista:", len(lista))
print("lista[0:2]:", lista[0:2])
print("lista[0:3]:", lista[0:3])
lista_fatiada = lista[0:3]
print(lista_fatiada)

# Adicionar e remover elementos da lista
lista.append("ola")
print(lista)

lista.remove(3)
print(lista)
print("lista[0:3]:", lista[0:3])

# Dicionários
dicionario = {"nome": "Gabriel", "idade": 30}
print("nome:", dicionario["nome"])
print("idade:", dicionario["idade"])

dicionario["altura"] = "180 cm"
print("altura:", dicionario["altura"])
dicionario["sobrenome"] = "Casemiro"
print("sobrenome:", dicionario["sobrenome"])

# Loop for
print("Iterando sobre a lista:")
for elemento in lista:
    print(elemento)

# Loop while
contador = 0
while contador < len(lista):
    print(lista[contador])
    contador += 1

# Condicionais
idade = 20
print("idade:", idade)
if idade >= 18:
    print("O usuário é maior de idade")
else:
    print("O usuário é menor de idade")

# Funções
def saudacao(nome):
    print("Olá,", nome)

saudacao("Gabriel")
saudacao("João")
saudacao("Guilherme")

def somar_valores(numero1, numero2):
    return numero1 + numero2

numero1 = 2
numero2 = 5
valor = somar_valores(numero1, numero2)

print(f"Soma {numero1} + {numero2} = {valor}")