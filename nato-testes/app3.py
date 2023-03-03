realtxt = "O que é real? Como você define o 'real'? Se \
              você está falando sobre o que você pode sentir,\
              o que você pode cheirar, o que você pode saborear e\
              ver, o real são simplesmente sinais elétricos interpretados\
              pelo seu cérebro. (filme Matrix)"
keeper = realtxt.strip(".,()").upper()
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


texto = []
texto.append(keeper)
text_in = " "
for palavras in texto:
    for palavras in palavras:
        if palavras in alfabeto_nato:
            text_in += f"{palavras} : {alfabeto_nato[palavras]}, "

print(text_in)