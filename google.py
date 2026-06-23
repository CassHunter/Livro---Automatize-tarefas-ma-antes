# abre pesquisa no google com arg no terminal ou conteudo do clipboard
import sys, pyperclip, urllib.parse, webbrowser


if len(sys.argv)>1:
    entrada = ' '.join(sys.argv[1:])
else:
    entrada = pyperclip.paste()

entrada = urllib.parse.quote(entrada)



webbrowser.open(f'http://google.com/search?q={entrada}')