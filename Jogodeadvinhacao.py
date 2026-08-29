
# O trecho abaixo sorteia um número inteiro no intervalo [1,20]
import random
semente = int(input("Digite a semente do sorteio: "))
random.seed(semente)
numero_sorteado = random.randint(1,20)


import random

semente = int(input("Digite a semente do sorteio: "))
random.seed(semente)
numero_sorteado = random.randint(1, 20)

print("Escolhi um inteiro entre 1 e 20. Adivinhe-o!")

acertou = False
tentativa = 1

while tentativa <= 5 and not acertou:
    chute = int(input("Seu chute: "))
    
    if chute == numero_sorteado:
        print(f"Legal, acertou na tentativa {tentativa}")
        acertou = True
    else:
        if chute > numero_sorteado:
            print("Chutou alto")
        else:
            print("Chutou baixo")
            
        # Dica de paridade se a paridade do chute for diferente da do número sorteado
        if chute % 2 != numero_sorteado % 2:
            if numero_sorteado % 2 == 0:
                print("Tente um par")
            else:
                print("Tente um impar")
                
        tentativa += 1

if not acertou:
    print("Tentativas esgotadas!")
    print(f"O escolhido foi o {numero_sorteado}")


