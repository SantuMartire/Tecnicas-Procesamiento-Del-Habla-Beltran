from nltk.stem import PorterStemmer

ps = PorterStemmer()
palabras = ["program","programming","programer","programs","programmed"]
for palabra in palabras:
    print(palabra, "\t", ps.stem(palabra))