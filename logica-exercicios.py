
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





