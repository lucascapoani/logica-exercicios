
"""
Ler dois números e imprimir as variáveis na mesma ordem que foram digitadas.
"""

v1 = input ("Digite um número: ")
v2 = input ("Digite outro número: ")

print ("v1=",v1,"v2=",v2)

print ("Voce digitou ", v1, " e ", v2)
print (f"v1= {v1} v2= {v2}")

#-----------------------------------------------------------------------------#


"""
Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas
variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa. Mostrar o
conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca.
"""

vA = input ("Digite o primeiro número: ")
vB = input ("Digite o segundo número: ")

print ("Antes da troca")
print (f"vA = {vA}    vB = {vB}")


vA, vB = vB, vA

# maneira genérica de realizar a troca dos conteúdos
#vC = vA
#vA = vB
#vB = vC

print ("Após a troca")
print (f"vA = {vA}    vB = {vB}")


#----------------------------------------------------------------------------#

"""
Ler dois valores numéricos e escrever a soma destes.
"""

vA =  input ("Digite o primeiro valor: ")
vB =  input ("Digite o segundo valor: ")


print (f"Resultado = {float(vA) + float(vB)}")


#----------------------------------------------------------------------------#


"""
Ler tres valores numericos e escrever a media aritmetica
"""



vA = int(input ("Digite o primeiro número: "))
vB = int(input ("Digite o segundo número: "))
vC = int(input ("Digite o terceiro número: "))

soma = vA + vB + vC
media = (soma) / 3

print (f"A soma das variáveis é {soma} e a média é {media}")

#----------------------------------------------------------------------------#


"""
Ler um conjunto de 5 dados numéricos e imprimir sua soma e sua média
"""


soma = 0
for i in range (1,6):
    n = int(input("Digite "+str(i)+" número: "))
    soma = soma + n
    
media = soma / i

print (f"Soma = {soma}  Média = {media} ")



"""   
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))

soma = n1+n2+n3+n4+n5

media = soma / 5

print (f"Soma = {soma}  Média = {media} ")
"""


#----------------------------------------------------------------------------#


'''
Fazer um algoritmo para ler dois números e mostrar o maior deles.

'''


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))


if n1 > n2:
    print (f"O maior é {n1}")
elif n2 > n1:
    print (f"O maior é {n2}")
else:
    print ("Números iguais")

#----------------------------------------------------------------------------#

"""
8. Faça um algoritmo que leia valores para as variáveis a, b e c e mostre o resultado da seguinte
expressão:
( a – b ) * c
"""

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

res = (a - b) * c

print (f"O resultado é {res}")

#------------------------------------------------------------------------------#

"""
9. Faça um algoritmo que mostre o resultado da expressão abaixo:
(( x – 5) * y) – z
"""

x = int(input("Digite o valor para x: "))
y = int(input("Digite o valor para y: "))
z = int(input("Digite o valor para z: "))

res = ((x-5)*y)-z

print (f"O resultado da expressão ((x-5)*y)z é {res}")

#------------------------------------------------------------------------------#

"""
10. Calcular a média ponderada das notas
"""

n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))
p1 = int(input("Peso da nota 1: "))
p2 = int(input("Peso da nota 2: "))

mp = ((n1*p1)+(n2*p2))/(p1+p2)

print (f"A media ponderada do aluno é {mp}")

#------------------------------------------------------------------------------#

"""
11. Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus
Centígrados.
"""

f = int(input("Digite a temperatura em Fahrenheit: "))

c = ((f-32)*5)/9

print (f"A temperatura em graus Centígrados é de {c}")

#------------------------------------------------------------------------------#

"""
12. Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer
uma viagem até a casa de sua irmã.
Dados extras:
- Distância da casa de Maria até sua irmã : 520 km
- Seu carro consome 12 Km/litro de combustível.
- Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 4,50 o litro.
Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o valor do litro de
combustível, com estes dados o algoritmo deverá calcular a quantidade de litros de combustível para a
viagem e o custo da viagem.
"""

d = int(input("Digite a distância do seu destino (km): "))
c = float(input("Digite o consumo do seu carro (km/L): "))
g = float(input("Digite o valor do litro de combustível (R$): "))

calc = d/c

print(f"Você vai precisar de {calc} litros de gasolina")



#-----------------------------------------------------------------------------#

"""
Faça um algorítmo que leia, para 8 pessoas, seus nomes e idades.
Após, mostre o nome e a idade da pessoa mais nova.
Obs: Não utilizar listas
"""

idadeMaisNovo = 999

for qtPessoas in range (8):
    nome = input ("Nome: ")
    idade = int(input ("Idade: "))

    if qtPessoas ==0 or idade < idadeMaisNovo:        
        idadeMaisNovo = idade
        nomeMaisNovo = nome

print(f"Pessoa mais nova: {nomeMaisNovo}, possui {idadeMaisNovo} de idade. ")

#----------------------------------------------------------------------------#

"""
Faça um algorítmo que leia, para X pessoas, seus nomes e idades.
Após, mostre o nome e a idade da pessoa mais nova.
Obs: Não utilizar listas
"""

primeiraDigitacao = True

while True:
    print("[sair] - finaliza")
    nome = input ("Nome: ")
    if nome == 'sair':
        break #break finaliza um laço de repetição
    
    idade = int(input ("Idade: "))

    if primeiraDigitacao or idade < idadeMaisNovo:        
        idadeMaisNovo = idade
        nomeMaisNovo = nome
        primeiraDigitacao = False

print(f"Pessoa mais nova: {nomeMaisNovo}, possui {idadeMaisNovo} de idade. ")

#----------------------------------------------------------------------------#




