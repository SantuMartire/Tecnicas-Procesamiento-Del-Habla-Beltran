import nltk

from nltk.corpus import stopwords
import string
from nltk import word_tokenize

def quitarStopwords_esp(texto):
    espaniol = stopwords.words("spanish")
    texto_limpio = [w.lower() for w in texto if w.lower() not in espaniol and w not in string.punctuation]
    return texto_limpio

def quitarStopwords_eng(texto):
    ingles = stopwords.words("english")
    texto_limpio = [w.lower() for w in texto if w.lower() not in ingles and w not in string.punctuation]
    return texto_limpio

text = "El verdadero peligro no es que las computadoras empiecen a pensar como hombres, sino que los hombres empiecen a pensar como computadoras. Sydney G. Harris"
text_tokenizado = word_tokenize(text)

print(text_tokenizado)

print(quitarStopwords_esp(text_tokenizado))