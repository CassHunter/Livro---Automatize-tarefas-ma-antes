import os, re

# Solicita a expressão regular
padrao = input('Digite a expressão regular: ')
regex = re.compile(padrao)

# Percorre todos os arquivos da pasta atual
for nome_arquivo in os.listdir():

    # Verifica se termina com .txt
    if nome_arquivo.endswith('.txt'):
        print(f'\n=== {nome_arquivo} ===')
        with open(nome_arquivo, encoding='utf-8') as file:
            # Lê linha por linha
            for numero_linha, linha in enumerate(file, start=1):
                # Procura o padrão na linha
                if regex.search(linha):
                    print(f'Linha {numero_linha}: {linha.strip()}')
                else:
                    print('não encontrado.')