# Abre pag google tradutor, traduzindo arg da linha de comando ou do clipboard
# tradução: pt - en

import webbrowser, sys, pyperclip, urllib.parse
idiomas = {'en pt':'https://translate.google.com.br/?sl=en&tl=pt&text={}',
           'pt en':'https://translate.google.com.br/?sl=pt&tl=en&text={}',
           'es pt':'https://translate.google.com.br/?sl=es&tl=pt&text={}',
           'fr pt':'https://translate.google.com.br/?sl=fr&tl=pt&text={}',}

if len(sys.argv)>1 and sys.argv[1].lower()=='help':
      print('''------------------
Uso:
tradutor.py (texto)
    Traduz clipboard ou texto pt -> en

tradutor.py en pt (texto)
    Inglês -> Português
            
Idiomas:
pt - Português
en - Inglês
es - Espanhol
fr - Francês
------------------''')
      sys.exit()   #termina o programa

idioma = 'en pt'

if len(sys.argv) == 1:   #pesquisa default clipboard(padrao) OK
    texto = pyperclip.paste()

elif len(sys.argv) >= 3 and ' '.join(sys.argv[1:3]).lower() in idiomas:
    idioma = ' '.join(sys.argv[1:3]).lower()
    if len(sys.argv) == 3:
        texto = pyperclip.paste()
    else:
        texto = ' '.join(sys.argv[3:])  
else:
    texto = ' '.join(sys.argv[1:])

texto = urllib.parse.quote(texto)  # converte texto para URL segura
webbrowser.open(idiomas[idioma].format(texto))
