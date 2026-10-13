def obtemPalavrasProximas(palavra, vocabulario):
    palavras_proximas = []
    for i in range(len(palavra)):
        for c in "abcdefghijklmnopqrstuvwxyz":
            prox_palavra = palavra[:i] + c + palavra[i+1:]
            if prox_palavra in vocabulario and prox_palavra != palavra:    
                palavras_proximas.append(prox_palavra)
    return palavras_proximas


def criaArvoreDeBusca(inicio, fim, vocabulario):
    inicioFila = 0

    fila = [[inicio, -1]]
  
    # Faz uma "busca em largura" usando fila
    while inicioFila < len(fila): # enquanto ainda tem elemento na fila
        palavra = fila[inicioFila][0]
        inicioFila += 1
        
        proximas = obtemPalavrasProximas(palavra,vocabulario)
        for prox_palavra in proximas:
            if not pertenceArvore(prox_palavra, fila):
                fila.append([prox_palavra,inicioFila-1])
                                    
                # Se achou a palavra, para de inserir nós na árvore
                if prox_palavra == fim:
                    return fila
                
    return fila
    

def obtemCaminho(inicio, fim, vocabulario):
    arvore = criaArvoreDeBusca(inicio, fim, vocabulario)
    
    if arvore[-1][0] != fim:
        return []
    
    pos = len(arvore)-1
    l = []
    while pos >= 0:
        l.append(arvore[pos][0])
        pos = arvore[pos][1]
        
    l.reverse()
    
    return l




def pertenceArvore(palavra,arvore):
    for no in arvore:
        if no[0] == palavra:
            return True
        
    return False
    

 
def main():
    
    # Nome e caminho do arquivo de vocabulário
    nome_arquivo = "./vocabulario.txt"
       
    # Leitura do vocabulário
    arquivo = open(nome_arquivo, 'r')
    vocabulario = arquivo.readlines()
    arquivo.close()

    # Remove a quebra de linha '\n' do final das palavras lidas
    for i in range(len(vocabulario)):
        vocabulario[i] = vocabulario[i].rstrip()

    opcao = 1
    while opcao != 0:
        opcao = int(input("Digite a opcao: "))
        
        if opcao == 1:
            ### Teste da função obtemPalavrasProximas
            palavra = input("Digite uma palavra: ")
            proximas = obtemPalavrasProximas(palavra, vocabulario)
            print("Palavras proximas de %s: %s" %(palavra, proximas))
            
        elif opcao == 2:
            ### Teste da função criaArvoreDeBusca
            inicio = input("Digite a palavra de inicio: ")
            fim = input("Digite a palavra de fim: ")
            arvore = criaArvoreDeBusca(inicio, fim, vocabulario)
            print("Quantidade de nos da arvore:", len(arvore))            
            print("Arvore:", arvore)
    
        elif opcao == 3:
            ### Teste da função obtemCaminho            
            inicio = input("Digite a palavra de inicio: ")
            fim = input("Digite a palavra de fim: ")            
            caminho = obtemCaminho(inicio, fim, vocabulario)
            
            if len(caminho) == 0:
                print("Nao existe caminho entre %s e %s"%(inicio, fim))
            else:
                print ("A distancia entre %s e %s é %d"%(inicio, fim, len(caminho)-1))
    
                str_caminho = caminho[0]
                for i in range(1,len(caminho)):
                    str_caminho += " -> " + caminho[i]
                print(str_caminho)
                
    return
                
                
# NAO REMOVA AS LINHAS A SEGUIR
if __name__ == '__main__':
    main()
