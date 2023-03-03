import time 
import unicodedata
import re
import datetime

realtxt = "O que é real? Como você define o 'real'? Se \
              você está falando sobre o que você pode sentir,\
              o que você pode cheirar, o que você pode saborear e\
              ver, o real são simplesmente sinais elétricos interpretados\
              pelo seu cérebro. (filme Matrix)"
alfabeto_nato = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

agora = datetime.datetime.now() 
for palavra in realtxt.split():
    processamento_2 = unicodedata.normalize("NFD", palavra).encode("ascii", "ignore").decode("utf-8")
    processamento_3 = re.sub('[^A-Za-z0-9]+', "", processamento_2)
    caracteres = []
    for letra in list(processamento_3):
        caracteres.append(alfabeto_nato[letra.upper()])
    print(f"{palavra.rjust(15)} : {caracteres}")
milissegundos = agora.strftime("%f")[:-3]  
print(milissegundos)
