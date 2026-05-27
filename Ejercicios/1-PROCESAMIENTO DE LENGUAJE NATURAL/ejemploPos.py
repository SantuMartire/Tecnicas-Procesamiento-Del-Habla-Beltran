#Instalar spaCy y el modelo en español
#pip install spacy
#python -m spacy download es_core_news_sm

import spacy

# Cargar el modelo de español
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo
#texto = "El perro corre rápidamente por el parque."
texto = "La mariposa amarilla revolotea en el jardín"

# Procesar el texto
doc = nlp(texto)


# Mostrar cada palabra con su POS
for token in doc:
    print(token.idx)
    print(token.text, "→", token.pos_)



'''
Etiqueta        Nombre                      Significado / Ejemplos
ADJ             Adjetivo                    bonito, grande, feliz
ADP             Adposición (preposición)    a, ante, con, para, sin
ADV             Adverbio                    rápidamente, muy, hoy, aquí
AUX             Verbo auxiliar              haber, estar, ser (cuando actúan como auxiliares)
CCONJ           Conjunción coordinante      y, o, pero, aunque
DET             Determinante                el, la, los, unas, mi, su
INTJ            Interjección                ¡ay!, hola, eh
NOUN            Sustantivo                  perro, casa, computadora, Juan
NUM             Número                      uno, dos, primero, 100
PART            Partícula                   no, más, menos (cuando no son adverbios)
PRON            Pronombre                   yo, tú, él, nosotros, esto
PROPN           Nombre propio               Argentina, María, Google
PUNCT           Signo de puntuación         ., ; ? !
SCONJ           Conjunción subordinante     porque, aunque, cuando
SYM             Símbolo                     %, $, #
VERB            Verbo                       correr, estudiar, escribir
X               Otros / Desconocido         palabras extranjeras o no clasificables

'''


'''
Cada vez que ejecutás:
doc = nlp(texto)

spaCy hace internamente, en este orden:
Tokenización → divide el texto en palabras, signos, números, etc.
Asignación de POS → etiquetas gramaticales.
Lematización → forma base de cada palabra.
Dependencias sintácticas → árbol gramatical.
NER (si el modelo lo tiene) → entidades como PERSONA, LUGAR, etc.

La tokenización siempre es el primer paso.
'''