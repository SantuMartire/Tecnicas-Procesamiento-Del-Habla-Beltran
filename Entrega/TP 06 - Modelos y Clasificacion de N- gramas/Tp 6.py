#
#TP 06 - Modelos y Clasificación de N-gramas
#El archivo CorpusEducacion.txt es un resumen de las opiniones reales de alumnos de Colombia que expresan
#sus deseos con respecto a la educación superior en el año 2025.
#Dado el corpus del archivo CorpusEducacion.txt, obtener en gráfico de barras la comparación entre 2-gramas
#y 3-gramas luego de preparar el texto con tokens, lemas y stop_words. Organizar el código con funciones.
#Definir la cantidad de apariciones de las palabras en 2 (min_df = 2).
#
#

from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import os

def quitarStopwords_esp(texto):
    espaniol = stopwords.words("spanish")
    texto_limpio = [w.lower() for w in texto if w.lower() not in espaniol and w not in string.punctuation]
    return texto_limpio

corpus = []
with open(os.path.join(os.path.dirname(__file__), "CorpusEducacion.txt"), "r", encoding="cp1252") as file:
    for line in file:
        corpus.append(" ".join(quitarStopwords_esp(word_tokenize(line))))

print("CORPUS")
print(corpus)

#/************************************/
#N-gramas
#min_df=2 -> cuantas apariciones debe superar la palabra
#ngram_range=(2,3) -> toma combinaciones de 2 o 3 n-gramas
vectorizer = CountVectorizer(ngram_range=(2,3), min_df=2)
#fit.transform() para transformar los datos
X = vectorizer.fit_transform(corpus)
print("ARREGLO en forma de array")
print(X.toarray())

#graficar los n-gramas
#get_feature_names_out() -> se accede al indice de cada palabra
print("N-GRAMAS DE VECTOR")
print(vectorizer.get_feature_names_out())
df = pd.DataFrame(X.sum(axis=0).T,
                  index=vectorizer.get_feature_names_out(),
                  columns=['freq']).sort_values(by='freq', ascending=True)

n = len(df)
fig, ax = plt.subplots(figsize=(10, max(6, n * 0.35)))
df.plot(kind='barh', title='N-Gramas', ax=ax)
ax.tick_params(axis='y', labelsize=9)
plt.tight_layout()
plt.show()