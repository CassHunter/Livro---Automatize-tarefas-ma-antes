# Inicia um mapa no navegador usando um enedereço da linha de comando ou do clipboard

import webbrowser, sys, pyperclip, urllib.parse
if len (sys.argv)>1:
    #obtem o endereço da linha de comando
    endereco = ' '.join(sys.argv[1:])
else:
    #obtém o endereço do clipboard
    endereco = pyperclip.paste()

endereco = urllib.parse.quote(endereco)  # converte texto para URL segura
webbrowser.open(f'http://maps.google.com/maps/place/{endereco}')