# %%
import re, pyperclip

regex = re.compile(r'\d{9}')

texto = pyperclip.paste()


print(regex.findall(texto))