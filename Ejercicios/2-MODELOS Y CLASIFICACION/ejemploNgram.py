#Aplicar stop_word, lematizaciòn y buscar 2/3-gramas en un corpus para su analisis.
#predecir la palabra más probable que podría seguir una secuencia, encontrando la distribución de probabilidad en secuencias de palabras
#Analizarlo
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

def quitarStopwords_eng(texto):
    ingles = stopwords.words("english")
    texto_limpio = [w.lower() for w in texto if w.lower() not in ingles 
                    and w not in string.punctuation 
                    and w not in ["'s", '|', '--', "''", "``", "-", ".-", "."] ]
    return str(texto_limpio)


#Definir el corpus de texto
corpus = [quitarStopwords_eng(word_tokenize("Python is an interpreted and high-level language, while CPlus is a compiled and low-level language .-"))
,quitarStopwords_eng(word_tokenize("JavaScript runs in web browsers, while Python is used in various applications, including data science and artificial intelligence."))
,quitarStopwords_eng(word_tokenize("JavaScript is dynamically and weakly typed, while Rust is statically typed and ensures greater data security .-"))
,quitarStopwords_eng(word_tokenize("Python and JavaScript are interpreted languages, while Java, CPlus, and Rust require compilation before execution."))
,quitarStopwords_eng(word_tokenize("JavaScript is widely used in web development, while Go is ideal for servers and cloud applications."))
,quitarStopwords_eng(word_tokenize("Python is slower than CPlus and Rust due to its interpreted nature."))
,quitarStopwords_eng(word_tokenize("JavaScript has a strong ecosystem with Node.js for backend development, while Python is widely used in data science .-"))
,quitarStopwords_eng(word_tokenize("JavaScript does not require compilation, while CPlus and Rust require code compilation before execution .-"))
,quitarStopwords_eng(word_tokenize("Python and JavaScript have large communities and an extensive number of available libraries."))
,quitarStopwords_eng(word_tokenize("Python is ideal for beginners, while Rust and CPlus are more suitable for experienced programmers."))
]
print("CORPUS")
print(corpus)

#/************************************/
#N-gramas
#min_df=20 -> cuantas apariciones debe superar la palabra
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
pd.DataFrame(X.sum(axis=0).T,
             index=vectorizer.get_feature_names_out(),
             columns=['freq']).sort_values(by='freq',
                                            ascending=True).plot(kind='barh', title='N-Gramas')

plt.show()
