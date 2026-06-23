# abre pesquisa no google com arg no terminal ou conteudo do clipboard
# usa seletores de site:
# g - google / y - youtube / w - wikipedia / f - adorocinema

import sys, pyperclip, webbrowser
from urllib.parse import quote

sites = {
    'g': 'http://google.com/search?q={}',
    'y': 'https://www.youtube.com/results?search_query={}',
    'w': 'https://pt.wikipedia.org/wiki/{}',
    'f': 'https://www.adorocinema.com/pesquisar/?q={}',
    'r': 'https://www.reddit.com/search/?q={}'
}

if len(sys.argv)>1 and sys.argv[1].lower()=='list':
    print('''------------------
g - Google
y - Youtube
w - Wikipédia
f - AdoroCinema
r - reddit
------------------''')
    sys.exit()   #termina o programa

# seletores = ('g', 'y', 'w', 'f', 'r')

if len(sys.argv) == 1:   #pesquisa google clipboard(padrao) OK
    site = 'g'
    entrada = pyperclip.paste()


elif len(sys.argv) == 2 and sys.argv[1] in sites:
    site = sys.argv[1].lower()
    entrada = pyperclip.paste()

elif sys.argv[1].lower() in sites:   #pesquisa site com argumentos
    site = sys.argv[1].lower()   # NÃO ESQUECER DE FECHAR PARENTESES!!!!
    entrada = ' '.join(sys.argv[2:])

else:    #pesquisa google com argumentos(padrao) OK
    site = 'g'
    entrada = ' '.join(sys.argv[1:])

entrada = quote(entrada)
webbrowser.open(sites[site].format(entrada))

# if site == 'g':
#     webbrowser.open(f'http://google.com/search?q={entrada}')
# elif site == 'y':
#     webbrowser.open(f'https://www.youtube.com/results?search_query={entrada}')
# elif site == 'w':
#     webbrowser.open(f'https://pt.wikipedia.org/wiki/{entrada}')
# elif site == 'f':
#     webbrowser.open(f'https://www.adorocinema.com/pesquisar/?q={entrada}')

# como posso add um quinto site sem criar mais um elif? --> dicionários!!

