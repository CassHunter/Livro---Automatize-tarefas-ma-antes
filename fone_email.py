import pyperclip, re

# fazer: criar regex para telefone Eua
foneEua = re.compile(r'''
                     (
                     (\d{3}|\(\d{3}\))    # código de área
                     (\s|-|\.)?    # separador
                     (\d{3})   #primeiros 3 digitos
                     (\s|-|\.)  # separador
                     (\d{4})  # últimos 4 dígitos
                     (\s*(ext|x|est.)\s*(\d{2,5}))?   # extensão
                     )''', re.VERBOSE)

# fazer: criar regex para telefone Br
foneBr = re.compile(r'''
                    (\+55\s?)?   # código pais +55
                    \s*
                    (\(\d{2}\)|\d{2})?    # cód de área DDD 2 dig
                    \s*
                    (9?\d{4})   # 4 primeiros dig (dig extra - 9 em celulares)
                    [\s-]?    # - separação
                    (\d{4})    #4 ultimos dig
                    ''',re.VERBOSE)

# fazer: cria a regex para email
emailRgx = re.compile(r'''(
                      [a-zA-Z0-9._%+-]+   # nome do usuário
                      @    # símbolo @
                      [a-zA-Z0-9.-]+   #nome do domínio
                      (?:\.[a-zA-Z]{2,4})+   #ponto seguido de outros caracteres
                      )''', re.VERBOSE)

# fazer: Encontrar correspondencias no texto do clipboard
text = str(pyperclip.paste())

matches_foneEua = []
for groups in foneEua.findall(text):
    foneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        foneNum += ' x'+groups[8]
    matches_foneEua.append(foneNum)

matches_foneBr = []
for groups in foneBr.findall(text):
    foneNum = '-'.join([groups[1], groups[2], groups[3]])
    matches_foneBr.append(foneNum)

matches_email = []
for groups in emailRgx.findall(text):
    matches_email.append(groups[0])

# formatação da string final ##
# stringFinal = ''
# stringFinal += 'Telefones EUA encontrados:\n'

# if matches_foneEua:
#     stringFinal += '\n'.join(matches_foneEua)

# stringFinal += '\n\nTelefones BR encontrados:\n'
# if matches_foneBr:
#     stringFinal += '\n'.join(matches_foneBr)

# stringFinal += '\n\nEndereços de email encontrados:\n'
# if matches_email:
#     stringFinal +='\n'.join(matches_email)

# Simplificação formação de stringFinal ---------
stringFinal = (
    'Telefones EUA encontrados:\n'
    +'\n'.join(matches_foneEua)
    +'\n\nTelefones BR encontrados:\n'
    +'\n'.join(matches_foneBr)
    +'\n\nEndereços de email encontrados:\n'
    +'\n'.join(matches_email)
)

# copy --------------------------
if (len(matches_foneEua) or len(matches_foneBr) or len(matches_email))>0:
    pyperclip.copy(stringFinal)
    print('Copiado para clipboard: ')
    print(stringFinal)
else:
    print('No phone numbers or email addresses found.')





# fazer: Copiar os resultados para o clipboard
# if len(matches_foneEua) > 0:
#     pyperclip.copy('\n'.join(matches_foneEua))
#     print('Copied to clipboard: ')
#     print('\n'.join(matches_foneEua))
# else:
#     print('No phone numbers or email addresses found.')

