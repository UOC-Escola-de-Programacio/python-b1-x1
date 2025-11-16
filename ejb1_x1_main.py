"""El objetivo general del ejercicio es crear una serie de funciones que nos permitan realizar operaciones 
sobre un texto.

Para este ejercicio, no se debe usar la función split de Python. En vez de ello, deberás  usar las 
siguientes funciones auxiliares que serán de gran ayuda al resolver el ejercicio. Asimismo, se pueden 
elegir crear nuevas funciones adicionales. A continuación, presentaremos una descripción de estos métodos:

* is_newline(character): Es una función que detecta el final de una oración. Deberás suponer que las frases 
están separadas por "\n" (nueva línea). Si el carácter es este símbolo, devolverá True.

* is_space(character): Es una función que detecta si un carácter es un espacio en blanco. Si el carácter es 
este símbolo, devolverá True.

* remove_punctuation_marks(cad): Una función que elimina los signos de puntuación de una palabra o un texto. 
Este método devuelve como resultado una cadena de caracteres sin signos de puntuación.

Las funciones descritas en el apartado anterior forman parte del módulo denominado 'text_manager.py', por lo tanto, 
es preciso importar estas en el módulo 'ejb1_x1_main.py', el cual es el módulo principal en el que desarrollaremos 
nuestra solución. 
En este ejercicio utilizaremos  la variable "TEXT" de tipo cadena de caracteres(definida en el módulo text_manager.py), 
la cual será empleada en cada una de las siguientes funciones como parámetro. Los métodos que se solicita 
desarrollar son:

* find_largest_word(text): Un método que permite detectar la palabra más larga en un texto. Este método debe 
devolver como resultado una cadena de caracteres correspondiente a la palabra más larga. Al evaluar la palabra
no debe contener signos de puntuación. 

* is_palindrome_word(word): Es una función recursiva que nos permitirá detectar si una palabra es palíndromo. 
Un palíndromo es una palabra que se lee igual en un sentido que en otro. Por ejemplo las siguientes palabras son 
palíndromos: Ata; Aviva; Azuza; Apa; Afromorfa. Para el ejercicio, el texto se encuentra en lengua inglesa, 
por lo que no se requiere realizar ningún tipo de acción en relación con tildes o acentos. Al evaluar la palabra 
no debe contener signos de puntuación. El valor que devuelve es de tipo booleano. Si es un palíndromo devolverá 
"True", y en el caso contrario "False". 

* count_palindrome_words(text): Se trata de una función que nos permitirá enumerar las apariciones de palíndromos 
en el texto, por lo tanto, esta retorna un número entero. Para esto debemos hacer uso de la anterior 
función is_palindrome_word(word).

* find_size_largest_sentence(text, filter): Se trata de una función que permite encontrar el tamaño de la oración 
más larga cuyo valor de filtro esté en esa sentencia. Si no existe una oración que coincida con el filtro deberá 
lanzar una excepción del tipo ValueError. El valor a retornar es un número entero que representa la longitud de 
la cadena en cuestión. 
Por ejemplo: si se invoca a la función con los parámetros text = "Hola, Pepe.\n¿Cómo estás, amigo?", el parámetro
filter = "a", este debe devolver 19, ya que en la segunda oración "¿Cómo estás, amigo?", se encuentra incluido 
el valor pasado como filtro y la oración tiene una longitud de la cadena de texto más larga. 
"""
# Add your imports here
from util_package import text_manager

prueba = "esto es \n un texto \n"
TEXT = text_manager.TEXT
new_line = text_manager.is_newline
is_space = text_manager.is_space
remove_punct = text_manager.remove_punctuation_marks

def listar_lineas(text):
    lista = []
    linea = ""

    for i in text:
        if not new_line(i):
            linea +=i
        elif new_line(i):
            lista.append(linea)
            linea = ""
    
    return lista

    
def listar_palabras(text):
    lista = []
    palabra = ""

    
    for i in text:
        
        if not is_space(i) and not new_line(i):
            palabra += i
            
                
        else:
            lista.append(palabra)
            palabra = ""

    if palabra:
        lista.append(palabra)

     
    for index, i in enumerate(lista):

        lista[index] = remove_punct(lista[index])
        

    return lista


def find_largest_word(text):
    lista = listar_palabras(text)
    larga = ""
    for i in lista:
        if len(i) > len(larga):
            larga = i
    return str(larga)

    

def is_palindrome_word(word):
    # Write here your code
    
    for index, i in enumerate(word,1):

        if (word[index-1]).lower() != (word[-index]).lower():

            return False
        
        elif index < len(word):

            continue
        else:
            return True
    


def count_palindrome_words(text):
    # Write here your code
    
    print(text)
    palindrome_count = 0
    
    for i in listar_palabras(text):
        if is_palindrome_word(i) and len(i) > 1:
            print(i)
            palindrome_count += 1

    
    return int(palindrome_count)




def find_size_largest_sentence(text, filter):
    contador = 0
    larga = 0

    for i in listar_lineas(text):
        
        if filter in i:
            for e in i:
                contador += 1
            if contador > larga:
                larga = contador
                contador = 0
            else:
                contador = 0              
        elif not filter in text:
            raise ValueError
        
    return larga
    
    





# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
#print("La palabra mas larga es:", find_largest_word(TEXT))
#print(listar_lineas(TEXT))
#print(listar_palabras(TEXT))
#print("'reconocer' es un palíndromo su resultado es:", is_palindrome_word("reconocer"))
#print("'Casal' no un palíndromo su resultado es:", is_palindrome_word("Casal"))
#print("'a' es un palíndromo su resultado es:", is_palindrome_word("a"))
#print("'Ababa' es palíndromo su resultado es:", is_palindrome_word("Ababa"))
print("El número de palabras identificadas como palíndromos es:", count_palindrome_words("a r e r\nAta; Azuza; Apa; aa rr"))
#print("El tamaño de la oración más larga con el filtro='a', es :", find_size_largest_sentence(TEXT, filter="a"))
