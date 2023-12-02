import googlesearch
import os
from googlesearch import search 

def color_text(text, color):
    colors = {
        'black': '\033[0;30m',
        'red': '\033[0;31m',
        'green': '\033[0;32m',
        'yellow': '\033[0;33m',
        'blue': '\033[0;34m',
        'magenta': '\033[0;35m',
        'cyan': '\033[0;36m',
        'white': '\033[0;37m',
        'bright_black': '\033[1;30m',
        'bright_red': '\033[1;31m',
        'bright_green': '\033[1;32m',
        'bright_yellow': '\033[1;33m',
        'bright_blue': '\033[1;34m',
        'bright_magenta': '\033[1;35m',
        'bright_cyan': '\033[1;36m',
        'bright_white': '\033[1;37m',
        'reset': '\033[0m'
    }

    if color in colors:
        return f"{colors[color]}{text}{colors['reset']}"
    else:
        return text

logo = """                                                                                              

     ▄█    ▄████████ ▀████    ▐████▀    ▄████████ ████████▄  ███    █▄    ▄▄▄▄███▄▄▄▄      ▄███████▄    ▄████████ 
    ███   ███    ███   ███▌   ████▀    ███    ███ ███   ▀███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ 
    ███   ███    █▀     ███  ▐███      ███    █▀  ███    ███ ███    ███ ███   ███   ███   ███    ███   ███    █▀  
    ███  ▄███▄▄▄        ▀███▄███▀     ▄███▄▄▄     ███    ███ ███    ███ ███   ███   ███   ███    ███   ███        
    ███ ▀▀███▀▀▀        ████▀██▄     ▀▀███▀▀▀     ███    ███ ███    ███ ███   ███   ███ ▀█████████▀  ▀███████████ 
    ███   ███    █▄    ▐███  ▀███      ███    █▄  ███    ███ ███    ███ ███   ███   ███   ███                 ███ 
    ███   ███    ███  ▄███     ███▄    ███    ███ ███   ▄███ ███    ███ ███   ███   ███   ███           ▄█    ███ 
█▄ ▄███   ██████████ ████       ███▄   ██████████ ████████▀  ████████▀   ▀█   ███   █▀   ▄████▀       ▄████████▀  
▀▀▀▀▀▀                                                                                                            
                             THIS TOOLS MAKE BY:JARJIT.EXE #KetapangGreyHat """
os.system('clear')       
print(color_text(f'{logo}', 'red'))
 
url = input(color_text(f'Masukan Url : ', 'green'))
file = input(color_text(f'Format File : ', 'green'))
list = file.split()
y = list
for i in y: 
    print(color_text(f'Mencari Info di {url} File {i}', 'bright_cyan'))
    for results in search(color_text(f'site:{url} jenis file:{i}', 'yellow', num=int(1), start=0, stop=None, pause=2)):
        print(results)