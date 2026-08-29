
import math
 
# Índices das colunas da tabela
COL_DATA = 0
COL_PREC = 1
COL_TEMP = 2
COL_UMID = 3
COL_VENTO = 4
COL_TEMPAPAR = 5
COL_MES = 6
COL_ANO = 7
COL_AEM = 8
 
TESTE_COLUNAS_AUXILIARES = False  # Se quiser ver as colunas para filtragem, mude para True.
 
MEDIDAS = {
    1: ("precipitação", COL_PREC),
    2: ("temperatura", COL_TEMP),
    3: ("umidade", COL_UMID),
    4: ("velocidade do vento", COL_VENTO),
    5: ("temperatura aparente", COL_TEMPAPAR),
}
 
 
# ---------------------------------------------------------------------
# Leitura dos dados
# ---------------------------------------------------------------------
def le_dados(nome_arquivo):
    """Lê o arquivo texto e devolve uma matriz (lista de listas) com as
    colunas Data, Prec, Temp, Umid, Vento. Entradas indisponíveis viram
    None."""
    tabela = []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            campos = linha.split()
            data = campos[0]
            medidas = []
            for campo in campos[1:5]:
                if campo == "None":
                    medidas.append(None)
                else:
                    medidas.append(float(campo))
            while len(medidas) < 4:
                medidas.append(None)
            tabela.append([data] + medidas)
    return tabela
 
 
# ---------------------------------------------------------------------
# Passo 1
# ---------------------------------------------------------------------
def temperatura_aparente(tabela):
    """Acrescenta a cada linha da tabela a temperatura aparente,
    calculada a partir de temperatura, umidade e velocidade do vento."""
    for linha in tabela:
        temp = linha[COL_TEMP]
        umid = linha[COL_UMID]
        vento = linha[COL_VENTO]
        if temp is None or umid is None or vento is None:
            linha.append(None)
        else:
            e = (umid / 100) * 6.105 * math.exp(17.27 * temp / (237.7 + temp))
            tempapar = temp + 0.33 * e - 0.70 * vento - 4.00
            linha.append(tempapar)
 
 
def acrescenta_colunas_para_filtragem(tabela):
    """Acrescenta a cada linha da tabela o mês, o ano e o valor aaaamm
    (AEM) extraídos da data, no formato dd/mm/aaaa."""
    for linha in tabela:
        dia, mes, ano = linha[COL_DATA].split("/")
        mes = int(mes)
        ano = int(ano)
        aem = ano * 100 + mes
        linha.append(mes)
        linha.append(ano)
        linha.append(aem)
 
    if TESTE_COLUNAS_AUXILIARES:
        imprime_tabela(tabela)
 
 
# ---------------------------------------------------------------------
# Passo 2
# ---------------------------------------------------------------------
def imprime_estatisticas(titulo, coluna_de_referencia, abscissas, medias, desvios):
    """Imprime a tabela de médias e desvios de 'titulo', usando
    'abscissas' (inteiros ou strings) como referência de cada linha."""
    cabecalho = "Ano" if coluna_de_referencia == "ANO" else "Mês"
    print(f"\nEstatísticas sobre {titulo}")
    print(f"{cabecalho:<8}média (desvio)")
    for absc, media, desvio in zip(abscissas, medias, desvios):
        media_str = ("%6.2f" % media) if media is not None else "%6s" % "-"
        desvio_str = ("(%.3f)" % desvio) if desvio is not None else "-"
        print(f"{str(absc):<8}{media_str} {desvio_str}")
 
 
def medias_e_desvios_de_medida(tabela, medida, coluna_de_referencia):
    """Calcula, para cada valor distinto de coluna_de_referencia, a
    média e o desvio padrão da coluna 'medida'. Devolve três listas:
    os valores da coluna_de_referencia, as médias e os desvios."""
    valores_ref = sorted({linha[coluna_de_referencia] for linha in tabela})
 
    medias = []
    desvios = []
    for valor in valores_ref:
        amostra = [
            linha[medida]
            for linha in tabela
            if linha[coluna_de_referencia] == valor and linha[medida] is not None
        ]
        n = len(amostra)
        if n == 0:
            media = None
            desvio = None
        else:
            media = sum(amostra) / n
            if n > 1:
                soma_quadrados = sum((x - media) ** 2 for x in amostra)
                desvio = math.sqrt(soma_quadrados / (n - 1))
            else:
                desvio = None
        medias.append(media)
        desvios.append(desvio)
 
    return valores_ref, medias, desvios
 
 
# ---------------------------------------------------------------------
# Passo 3
# ---------------------------------------------------------------------
def filtro_de_intervalo(tabela, j, v1, v2):
    """Devolve a subtabela com as linhas cujo valor na coluna j está
    entre v1 e v2 (inclusive)."""
    return [
        linha for linha in tabela
        if linha[j] is not None and v1 <= linha[j] <= v2
    ]
 
 
# ---------------------------------------------------------------------
# Auxiliares de impressão / entrada
# ---------------------------------------------------------------------
def imprime_tabela(tabela):
    cabecalhos = ["Data", "Prec", "Temp", "Umid", "Vento", "TempApar"]
    print(f"{cabecalhos[0]:<12}" + "".join(f"{c:>10}" for c in cabecalhos[1:]))
    colunas = [COL_PREC, COL_TEMP, COL_UMID, COL_VENTO, COL_TEMPAPAR]
    for linha in tabela:
        texto = f"{linha[COL_DATA]:<12}"
        for col in colunas:
            valor = linha[col] if col < len(linha) else None
            texto += f"{valor:10.2f}" if valor is not None else f"{'-':>10}"
        print(texto)
 
 
def imprime_menu():
    print("""
0. Termina o programa.
1. Imprime tabela.
2. Média de cada ano de uma das medidas.
3. Média de cada mês de uma das medidas.
4. Média de cada ano de uma das medidas em um período de tempo.
5. Média de cada mês de uma das medidas em um período de tempo.
6. Média de cada ano de uma das medidas em um mês específico.
7. Média por mês de uma das medidas em um período de tempo.""")
 
 
def escolhe_medida():
    print("\n1. Precipitação 2. Temperatura 3. Umidade 4. Velocidade do vento "
          "5. Temperatura aparente")
    opc = int(input("Medida escolhida: "))
    return MEDIDAS[opc]
 
 
def le_periodo():
    mes_i = int(input("Digite mês (1-12) do início do período: "))
    ano_i = int(input("Digite ano do início do período: "))
    mes_f = int(input("Digite mês (1-12) do fim do período: "))
    ano_f = int(input("Digite ano do fim do período: "))
    v1 = ano_i * 100 + mes_i
    v2 = ano_f * 100 + mes_f
    return v1, v2
 
 
def formata_aem(valor):
    """Converte um inteiro aaaamm em uma string 'm/aa' para exibição."""
    ano = valor // 100
    mes = valor % 100
    return f"{mes}/{ano % 100:02d}"
 
 
# ---------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------
def main():
    nome_arquivo = input("Digite o nome do arquivo de dados: ")
    tabela = le_dados(nome_arquivo)
    temperatura_aparente(tabela)
    acrescenta_colunas_para_filtragem(tabela)
 
    while True:
        imprime_menu()
        opc = int(input("Digite a sua escolha: "))
 
        if opc == 0:
            print("Tchau!")
            break
 
        elif opc == 1:
            imprime_tabela(tabela)
 
        elif opc == 2:
            print("\nImpressão de médias por ano")
            titulo, medida = escolhe_medida()
            abscissas, medias, desvios = medias_e_desvios_de_medida(
                tabela, medida, COL_ANO)
            imprime_estatisticas(titulo, "ANO", abscissas, medias, desvios)
 
        elif opc == 3:
            print("\nImpressão de médias por mês")
            titulo, medida = escolhe_medida()
            abscissas, medias, desvios = medias_e_desvios_de_medida(
                tabela, medida, COL_MES)
            imprime_estatisticas(titulo, "MES", abscissas, medias, desvios)
 
        elif opc == 4:
            print("\nImpressão de médias por ano num período")
            v1, v2 = le_periodo()
            subtabela = filtro_de_intervalo(tabela, COL_AEM, v1, v2)
            titulo, medida = escolhe_medida()
            abscissas, medias, desvios = medias_e_desvios_de_medida(
                subtabela, medida, COL_ANO)
            imprime_estatisticas(titulo, "ANO", abscissas, medias, desvios)
 
        elif opc == 5:
            print("\nImpressão de médias por mês num período")
            v1, v2 = le_periodo()
            subtabela = filtro_de_intervalo(tabela, COL_AEM, v1, v2)
            titulo, medida = escolhe_medida()
            abscissas, medias, desvios = medias_e_desvios_de_medida(
                subtabela, medida, COL_MES)
            imprime_estatisticas(titulo, "MES", abscissas, medias, desvios)
 
        elif opc == 6:
            print("\nImpressão de médias em um mês específico por ano")
            mes = int(input("Escolha o mês (1-12): "))
            subtabela = filtro_de_intervalo(tabela, COL_MES, mes, mes)
            titulo, medida = escolhe_medida()
            abscissas, medias, desvios = medias_e_desvios_de_medida(
                subtabela, medida, COL_ANO)
            imprime_estatisticas(titulo, "ANO", abscissas, medias, desvios)
 
        elif opc == 7:
            print("\nImpressão de médias por mês de uma das medidas em um "
                  "período de tempo")
            v1, v2 = le_periodo()
            subtabela = filtro_de_intervalo(tabela, COL_AEM, v1, v2)
            titulo, medida = escolhe_medida()
            abscissas, medias, desvios = medias_e_desvios_de_medida(
                subtabela, medida, COL_AEM)
            abscissas = [formata_aem(v) for v in abscissas]
            imprime_estatisticas(titulo, "AEM", abscissas, medias, desvios)
 
        else:
            print("Opção inválida!")
 
 
if __name__ == "__main__":
    main()