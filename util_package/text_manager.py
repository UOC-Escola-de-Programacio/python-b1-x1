import string

TEXT = '''
Are the following lines palindromes?
A man, a plan, a canal, Panama.
This line is not a palindrome
Don't nod
The next one might be my favorite
Taco Cat!
Another non-palindrome
Rats live on no evil star.
If your program finds this line, it's not working
Neil, a trap! Sid is part alien!
Step on no pets.
Dammit, I'm mad!
Madam, I'm Adam.
Madam, in Eden, I'm Adam.
Rise to vote, sir.
Never odd or even
If I had a hi-fi
Yo, banana boy!
Do geese see God?
No devil lived on.
Ah, Satan sees Natasha.
Lewd did I live & evil I did dwel!
A dog, a panic in a pagoda
Was it a cat I saw?
Was it a car or a cat I saw?
A Toyota's a Toyota.
Another non-palindrome
No lemons, no melon
Now I see bees, I won.
Ma is as selfless as I am.
Nurse, I spy gypsies-run!
The next one isn't as cool as the Panama one
A dog, a plan, a canal, pagoda
Was it Eliot's toilet I saw?
Some of these are hilarious. Papaya war?!
No, sir, away! A papaya war is on!
Go hang a salami, I'm a lasagna hog.
I, madam, I made radio! So I dared! Am I mad? Am I?
Swap God for a janitor, rot in a jar of dog paws.
Eva, can I see bees in a cave?
Not a palindrome
So many dynamos!
Red rum, sir, is murder.
'''

"""
is_new_line(character): Es una función que detecta el final de una oración. Deberás
suponer que las frases están separadas por "\n" (nueva línea). Si el carácter es este símbolo,
devolverá True.
"""

def is_newline(character):
    return character == "\n"
    
"""
is_space(character): Es una función que detecta si un carácter es un espacio en blanco.
Si el carácter es este símbolo, devolverá True.
"""
def is_space(character):
    return character == " "

"""
remove_punctuation_marks(cad): Una función que elimina los signos de puntuación de
una palabra o un texto. Este método devuelve como resultado una cadena de caracteres sin
signos de puntuación.
"""

def remove_punctuation_marks(cad):
    return cad.translate(str.maketrans('', '', string.punctuation))
