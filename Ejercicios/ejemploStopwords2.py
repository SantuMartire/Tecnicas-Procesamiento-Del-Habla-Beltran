import nltk

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import FreqDist
from nltk.corpus import stopwords
import string
from nltk import word_tokenize

def quitarStopwords_eng(texto):
    ingles = stopwords.words("english")
    texto_limpio = [w.lower() for w in texto if w.lower() not in ingles 
                    and w not in string.punctuation 
                    and w not in ["'s", '|', '--', "''", "``"] ]
    return texto_limpio

corpus = PlaintextCorpusReader(".", 'melville-moby_dick.txt')
texto_tokenizado = word_tokenize(corpus.raw())
#frecuencia=FreqDist(texto_tokenizado) #Sin quitar las stopwords
frecuencia=FreqDist(quitarStopwords_eng(texto_tokenizado)) #Quitando las stopwords
frecuencia.plot(20, show=True)
