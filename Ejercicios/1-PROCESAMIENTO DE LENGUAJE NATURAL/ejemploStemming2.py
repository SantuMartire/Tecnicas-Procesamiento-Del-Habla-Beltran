import nltk

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import FreqDist
from nltk.corpus import stopwords
import string
from nltk import word_tokenize
from nltk.stem import SnowballStemmer

def quitarStopwords_eng(texto):
    ingles = stopwords.words("english")
    texto_limpio = [w.lower() for w in texto if w.lower() not in ingles 
                    and w not in string.punctuation 
                    and w not in ["'s", '|', '--', "''", "``"] ]
    return texto_limpio

corpus = PlaintextCorpusReader(".", 'melville-moby_dick.txt') #Obtener texto de archivo
texto_tokenizado = word_tokenize(corpus.raw()) #Tokenizado del texto
frecuencia=FreqDist(quitarStopwords_eng(texto_tokenizado)) #Quitando las stopwords
ss = SnowballStemmer("english")
#stemming
for palabra in frecuencia.most_common(200):
    print(palabra[0], "\t", ss.stem(palabra[0])) #Realizando stemming a cada palabra
