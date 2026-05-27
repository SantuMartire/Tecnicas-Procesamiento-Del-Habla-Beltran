import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import FreqDist
from nltk.corpus import stopwords
import string
from nltk import word_tokenize

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def quitarStopwords_eng(texto):
    ingles = stopwords.words("english")
    texto_limpio = [w.lower() for w in texto if w.lower() not in ingles 
                    and w not in string.punctuation 
                    and w not in ["'s", '|', '--', "''", "``"] ]
    return texto_limpio

#Inicializar el Lematizador
lemmatizer = WordNetLemmatizer()

corpus = PlaintextCorpusReader(".", 'melville-moby_dick.txt') #Obtener texto de archivo
texto_tokenizado = word_tokenize(corpus.raw()) #Tokenizado del texto
frecuencia=FreqDist(quitarStopwords_eng(texto_tokenizado)) #Quitando las stopwords

#Sin Lematizar
for palabra in frecuencia.most_common(200):
    print(palabra[0]) 

print("-"*20)
#Lematizadas
for palabra in frecuencia.most_common(200):
    print(lemmatizer.lemmatize(palabra[0], get_wordnet_pos(palabra[0]))) #Realizando la lematizacion a cada palabra

