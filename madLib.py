with open('madlibs.txt') as f:
    texto = f.read()

    # localizar palavras ADJECTIVE, NOUN, VERB, ADVERB:
    marcadores = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']
    
    while True:
        proximo_marcador = None
        menor_posicao = len(texto)

        #Descobre qual marcador aparece primeiro no texto
        for marcador in marcadores:
            posicao = texto.find(marcador)

            if posicao != -1 and posicao < menor_posicao:
                menor_posicao = posicao
                proximo_marcador = marcador

        # não há mais marcadores
        if proximo_marcador is None:
            break

        resposta = input(f'Digite um {proximo_marcador}: ')

        texto = texto.replace(proximo_marcador, resposta, 1)

    print('\nTexto final:\n')
    print(texto)

    with open('resultado.txt', 'w', encoding='utf-8') as f:
        f.write(texto)





    