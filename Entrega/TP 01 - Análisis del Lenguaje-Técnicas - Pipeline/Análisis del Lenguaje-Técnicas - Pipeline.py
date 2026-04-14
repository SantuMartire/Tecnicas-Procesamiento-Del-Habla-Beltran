#TP 1
#Análisis del Lenguaje - Técnicas - Pipeline

""" Realizar una “canalización” o “pipeline” para analizar el siguiente corpus CorpusLenguajes.txt
-Aplicar stop_word,
-Lematización
-Tf-Idf
-Mostrar el corpus preparado
-Mostrar la matriz TF-IDF generada
-Mostrar el vocabulario generado
Analizar el mismo y redactar un informe con las conclusiones obtenidas.
-Obtener las jerarquía de 6 palabras mas usadas en todo el corpus
-La palabra menos utilizada
-Las palabras mas repetidas en la misma oración
-Imprimir el gráfico de Distribución de Frecuencia.
 """

# Importar las librerías necesarias
import os
import nltk
from nltk.corpus import stopwords
import string
from nltk import word_tokenize
from nltk import FreqDist

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

from sklearn.feature_extraction.text import TfidfVectorizer


#Importo el texto
directorio_actual = os.path.dirname(os.path.abspath(__file__)) 
ruta_archivo = os.path.join(directorio_actual, 'CorpusLenguajes.txt')

with open(ruta_archivo, 'r', encoding='utf-8') as file:
    corpus = file.read()
print("Texto cargado con éxito. \n")
print("\n", "-" * 75, "\n")

#Lo primero que hago es tokenizar el texto para luego eliminar las stopwords en español.
text_tokenizado = word_tokenize(corpus)
print(text_tokenizado)
print("\n", "-" * 75, "\n")
#Verifico que este tokenizado correctamente, luego aplico la función para eliminar las stopwords en español y los signos de puntuación.

#Elimino soptwords (En ingles porque el texto esta en ingles)
def quitarStopwords_eng(texto):
    ingles = stopwords.words("english")
    texto_limpio = [w.lower() for w in texto if w.lower() not in ingles
        and w not in string.punctuation
        and w not in ["'s", '|', '--', "''", "``"] ]
    return texto_limpio

print("Stopwords eliminados con éxito.\n \n")
print(quitarStopwords_eng(text_tokenizado))

print("\n", "-" * 75, "\n")
#Verifico que se hayan eliminado las stopwords y los signos de puntuación correctamente.
#nltk.download('wordnet')

texto_tokenizazdo = quitarStopwords_eng(text_tokenizado)

#Luego, aplico la lematización para reducir las palabras a su forma base.
def lematizar(texto):
    lemmatizer = WordNetLemmatizer()
    texto_lemmatizado = [lemmatizer.lemmatize(w) for w in texto]
    return texto_lemmatizado

#Y verifico que se haya aplicado la lematización correctamente. 
print("Lematización aplicada con éxito.\n \n")
print(lematizar(texto_tokenizazdo))

texto_lematizado = lematizar(texto_tokenizazdo)

print("\n", "-" * 75, "\n")

#Muestro la frecuencia de las palabras en el texto lematizado para luego graficar la distribución de frecuencia.
frecuencia=FreqDist(texto_lematizado)

frecuencia.plot(20, show=True)

print("\n", "-" * 75, "\n")


#Ahora, aplico la función para calcular el TF-IDF 
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texto_lematizado)

#Mostrar la matriz TF-IDF
print("Matriz TF-IDF:")
print(X.toarray())

#Mostrar el vocabulario generado
print("\nVocabulario:")
print(vectorizer.get_feature_names_out())


#Ahora busco las 6 palabras más usadas en todo el corpus, la palabra menos utilizada y las palabras más repetidas en la misma oración.
print("\n", "-" * 75, "\n")
print("Las 6 palabras más usadas en todo el corpus: \n")
frecuencia = FreqDist(texto_lematizado)
for mc in frecuencia.most_common(6):
    print(mc)

print("\n", "-" * 75, "\n")
print("La palabra menos utilizada: \n")
palabra_menos_utilizada = frecuencia.most_common()[-1]
print(palabra_menos_utilizada)

print("\n", "-" * 75, "\n")
print("Las palabras más repetidas en la misma oración: \n")

#Preguntar mañana a la profe :c
