
# Funções que devem ser implementadas sem alteracao de assinatura:

# Funcao 1 - Quantidade de pontos na borda
def pontosNaBorda(v0, v1, v2):
    # v0, v1, v2 são coordenadas dos vértices de um triângulo
         
   
   quantidade = 0
   if v0[0] == v1[0]:
      quantidade += modulo(v0[1],v1[1])
   elif v0[1] == v1[1]:
       quantidade += modulo(v0[0],v1[0])
   else :
         q1 = modulo(v0[1],v1[1])
         q2 = modulo(v0[0],v1[0])      
         quantidade += mdc(q1,q2) 
         
       
   if v1[0] == v2[0]:
       quantidade += modulo(v1[1],v2[1])
   elif v1[1] == v2[1]:
       quantidade += modulo(v1[0],v2[0])
   else :
         q1 = modulo(v1[0],v2[0])
         q2 = modulo(v1[1],v2[1])      
         quantidade += mdc(q1,q2) 

   
   if v2[0] == v0[0]:
        quantidade += modulo(v2[1],v0[1])
   elif v2[1] == v0[1]:
        quantidade += modulo(v2[0],v0[0])
   else :
         q1 = modulo(v2[0],v0[0])
         q2 = modulo(v2[1],v0[1])      
         quantidade += mdc(q1,q2)          
     
     
   return quantidade
    
     
    
     
def modulo(e,f):
         q = e - f
         if q < 0:
            q *= -1         
            return q
         else:
            return q


        
def mdc(t,w):   

    ant = t
    at    = w
    rest    = ant % at

    while rest != 0:
        ant = at
        at    = rest
        rest   = ant % at
    return at    
        
# Funcao 2 - Soma pontos na borda
def somaPontosNaBorda(alienigenas):
    # alienigenas é uma lista de triângulos
    quantidade = 0
    i = 0
    while i < len(alienigenas):
      quantidade += pontosNaBorda(alienigenas[i][0],alienigenas[i][1],alienigenas[i][2])   
      i += 1    
       
    return quantidade


# Funcao 3 - Ponto interno
def pontoInterno(ponto, v0, v1, v2):
    # ponto é a coordenada do ponto de uma munição
    # se ponto for interno:
    v = ponto
    v11 = [v1[0] - v0[0], v1[1] - v0[1]]
    v22 = [v2[0] - v0[0], v2[1] - v0[1]]
    
    a =   ( det( v, v22 ) - det( v0, v22 ) ) / det( v11,v22 )
    b = - ( det( v, v11 ) - det( v0, v11 ) ) / det( v11,v22 )
    
    if a > 0 and  b > 0 and a + b < 1 :  
        
       return True
    # caso contrário:
    else :
       
      return False


def pont(ponto):
   # converte a string lida em uma lista de inteiros
   ponto = ponto.split()
   for i in range(0,2):
    ponto[ i ] = int( ponto[ i ] )
   # separa as três coordenadas dos vértices do alienígena
   vz = [ ponto[0], ponto[1] ]
   return vz    

def det( m, n ): 
    
     return  m[0]*n[1] - m[1]*n[0]



# Funcao 4 - Limite de busca
def limitesDeBusca(v0, v1, v2):
    # v0, v1, v2 são coordenadas dos vértices de um triângulo
    busca = [v0[0], v0[1], v1[0], v1[1], v2[0], v2[1]]
    x_max = 0
    y_max = 0
    x_min = v0[0]
    y_min = v0[1]
    for i in range(0,5,2):
        if busca[i] > x_max:
           x_max = busca[i]   
    for j in range(1,6,2):
         if  busca[j] > y_max:       
           y_max = busca[j]
    
    for k in range(0,5,2):
        if busca[k] < x_min:
           x_min = busca[k]   
    for l in range(1,6,2):
        if  busca[l] < y_min:
           y_min = busca[l]  
               
           
    return x_min, y_min, x_max, y_max


# Funcao 5 - Pontos internos
def pontosInternos(v0, v1, v2):
    # v0, v1, v2 são coordenadas dos vértices de um triângulo
    quantidade = 0 
    w = limitesDeBusca(v0, v1, v2)      
    c = [w[0],w[1]]
    while c[1] <= w[3] :   
      c[0] = w[0]  
      while c[0] <= w[2]:
           if pontoInterno(c, v0, v1, v2) == True:
             quantidade += 1 
           c[0] += 1  
      c[1] += 1  
    
    return  quantidade





# Funcao 6 - Soma pontos internos
def somaPontosInternos(alienigenas):
    # alienigenas é uma lista de triângulos
    quantidade = 0
    i = 0
    while i < len(alienigenas):
      quantidade += pontosInternos(alienigenas[i][0],alienigenas[i][1],alienigenas[i][2])   
      i += 1   
	
    return quantidade




# Codigo para executar os testes:
def main():
    alienigenas = []
    n = int(input("Quantidade de alienigenas: "))
    for i in range(0,n):
        alienigenas.append( leAlienigena(i) )
        
    # Continue aqui o seu programa para testar as funcoes acima...
    a = int(input('Digite a funcao que deseja testar: '))
    while a != 0 : 
        
     if a== 1 : 
        z = int(input('Numero do alienigena:')) 
        print('Quantidade de pontos na borda:', pontosNaBorda(alienigenas[z][0],alienigenas[z][1],alienigenas[z][2]))
               
     elif a== 2:
         print('Soma de pontos na borda:', somaPontosNaBorda(alienigenas))
                
     elif a== 3:
         z = int(input('Numero do alienigena:'))
         print('Coordenadas do alienigena: (%d,%d), (%d,%d), (%d,%d)' %(alienigenas[z][0][0],alienigenas[z][0][1],alienigenas[z][1][0],alienigenas[z][1][1],alienigenas[z][2][0],alienigenas[z][2][1]))
         point = input('Coordenadas do ponto:')
         
         if pontoInterno(pont(point), alienigenas[z][0],alienigenas[z][1],alienigenas[z][2]) == True:
            print('Ponto interno ao triangulo!')
         else:    
            print('Ponto nao interno ao triangulo!')
     elif a== 4:
         z = int(input('Numero do alienigena:'))
         s = limitesDeBusca(alienigenas[z][0],alienigenas[z][1],alienigenas[z][2])
         
         print('Os limites são: (%d,%d) e (%d,%d)' %(s[0], s[1], s[2],s[3]))
        
                 
     elif a== 5:
         z = int(input('Numero do alienigena:'))
         
         print('Quantidade de pontos internos:',pontosInternos(alienigenas[z][0],alienigenas[z][1],alienigenas[z][2]))
              
     elif a== 6:     
         print('Soma de pontos internos:',somaPontosInternos(alienigenas))
         
         
     a = int(input('Digite a funcao que deseja testar: '))     
 
    


         
def leAlienigena(numero_alienigena):
  coordenadas = input("Alienigena %d: " %(numero_alienigena))
  # converte a string lida em uma lista de inteiros
  coordenadas = coordenadas.split()
  for i in range(0,6):
    coordenadas[ i ] = int( coordenadas[ i ] )
  # separa as três coordenadas dos vértices do alienígena
  v0 = [ coordenadas[0], coordenadas[1] ]
  v1 = [ coordenadas[2], coordenadas[3] ]
  v2 = [ coordenadas[4], coordenadas[5] ]
  return v0, v1, v2


           
# NAO REMOVA AS LINHAS A SEGUIR
if __name__ == '__main__':
    main()
    
