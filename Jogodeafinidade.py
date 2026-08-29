

## parâmetros para o método das congruências lineares:
m = 2**32
a = 22695477
c = 1
anterior = 42



"""
- O algoritmo soma() foi baseado em 
https://www.sanfoundry.com/python-program-find-sum-digits-number/
"""
def soma(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    if s > 9:
        return soma(s)
    return s


numJogadas = int(input("Digite o numero de jogadas:"))
i = 0
numAcertos = 0
while i < numJogadas: 
  i += 1
  n1 = int(input("Pessoa 1: digite um numero:"))
  soma(n1)  
  n2 = int(input("Pessoa 2: digite um numero:"))  
  soma(n2)      
  if soma(n1) == soma(n2):
     numAcertos += 1
afinidade = numAcertos / numJogadas 


sim = str(input("Deseja simular jogadas aleatorias (S/N)?"))
if sim == "S":
    i4 = 0
    i3 = 0
    while i4 < 10000:
      i4 += 1    
      i2 = 0
      numAcertos2 = 0
      while i2 < numJogadas:
        i2 += 1    
        n3 = (a * anterior + c) % m
        soma(n3)
        anterior = n3
        n4 = (a * anterior + c) % m
        soma(n4)
        anterior = n4
        if soma(n3) == soma(n4):
          numAcertos2 += 1
      if numAcertos2 >= numAcertos:
          i3 += 1
    p = i3 / 10000
    afinidade = 1 - p          
          
   
print("A afinidade de voces e de:",afinidade)
if afinidade >= 0 and afinidade< 1/3:
    print("A afinidade de voces e baixa. Que pena!")      
elif afinidade >= 1/3 and afinidade< 2/3:
    print("A afinidade de voces e mediana!")
else:
    print("Parabens! Voces tem uma bela afinidade!")      