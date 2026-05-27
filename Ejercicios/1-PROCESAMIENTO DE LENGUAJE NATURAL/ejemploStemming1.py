import nltk

from nltk.stem import SnowballStemmer

ss = SnowballStemmer("spanish")
palabras = ["corriendo", "corre", "corrí"]
for palabra in palabras:
    print(palabra, "\t", ss.stem(palabra))