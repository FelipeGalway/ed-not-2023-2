# função para calcular IMC
def calc_imc(peso, altura):
     return peso / altura ** 2

#maneira comum
# p = 85
# a = 1.72
# imc = calc_imc(p, a)
# print(imc) 

print(calc_imc(85, 1.72)) #maneira direta

###############################

from math import pi

"""
Função que calcula a área de uma figura geométrica plana
"""

def calc_area(base, altura, tipo):
     if tipo =="R": #Retangulo
          resultado = base * altura
     elif tipo == "T": #Triângulo
          resultado = base * altura / 2
     elif tipo == "E": #Eclipse
          resultado = (base/2) * (altura/2) * pi
     else: #Forma desconhecida
          resultado = None
     
     return resultado

print("Retângulo 20x30: ", calc_area(20,30,"R"))
print("Triângulo 45x32: ", calc_area(45,32,"T"))
print("Eclipse 10x15: ", calc_area(10,15,"E"))
print("Desconhecido 12x15: ", calc_area(12,16,"X"))

