def palavra_mais_frequente(arquivo):
    with open(arquivo, 'r') as arquivo_txt:
        texto = arquivo_txt.read()

        palavras = texto.split()

        contagem = {}
        for palavra in palavras:
            if palavra in contagem:
                contagem[palavra] += 1
            else:
                contagem[palavra] = 1
            
        palavra_mais_frequente = None
        contagem_mais_alta = 0
        for palavra, contagem_palavra in contagem.items():
            if contagem_palavra > contagem_mais_alta:
                palavra_mais_frequente = palavra
                contagem_mais_alta = contagem_palavra

        palavra = palavra_mais_frequente ("exemplo_davi")
        print(palavra)
        

        return palavra_mais_frequente