# Cria provas com perguntas e resposta em ordem aleatória, juntamente com 
# os gabaritos contendo as respostas.

import random

# Os dados para as provas. As chaves são os estados e os valroes são as capitais.
capitais = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':
'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky':
'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska':
'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon':
'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina':
'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington':
'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Gera 35 arquivos contendo as provas e gabaritos
for quizNum in range(35):

    # fazer: cria os arquivos com as provas e os gabaritos das respostas
    with open(f'capitaisquiz{quizNum+1}.txt', 'w') as quizFile, \
         open(f'capitaisquiz_respta{quizNum+1}.txt', 'w') as answerKeyFile:
        
        # fazer: Escreve o cabeçalho da prova.
        quizFile.write('Nome:\n\nData:\n\nPeriodo:\n\n')

        titulo = f'Quiz Capitais dos Estados Unidos (Form {quizNum + 1})'
        quizFile.write(titulo.center(60))    # centraliza o título

        quizFile.write('\n\n')


        # fazer: emparelha a ordem dos estados.
        estados = list(capitais.keys())   # transforma as keys do dicionario em lista
        random.shuffle(estados)

        # fazer: Percorre todos o 50 estado em um loop, criando uma pergunta para cada um.
        for questionNum in range(50):
            
            #Obtem respostas corretas e incorretas.
            respostaCerta = capitais[estados[questionNum]]
            respostaErrada = list(capitais.values())  # cria uma lista de todas values(capitais) do dicionario
            respostaErrada.remove(respostaCerta)

            respostaErrada = random.sample(respostaErrada, 3)  # escolhe 3 aleatoriamente sem repetir
            respostaOpcoes = respostaErrada + [respostaCerta] # formo as 4 opçoes 
            random.shuffle(respostaOpcoes)

            #Grava a pergunta e as opções de resposta  no arquivo de prova.
            quizFile.write(f'{questionNum + 1}. Qual a capital de {estados[questionNum]}?\n')

            for i in range(4):
                quizFile.write(f" ({'ABCD'[i]}). {respostaOpcoes[i]}\n")
            quizFile.write('\n')

            # Grava o gabarito com as resposta em um arquivo.
            answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[respostaOpcoes.index(respostaCerta)]}\n")
        