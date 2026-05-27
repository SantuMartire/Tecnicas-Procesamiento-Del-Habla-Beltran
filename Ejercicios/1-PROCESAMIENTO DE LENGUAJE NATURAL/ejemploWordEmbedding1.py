import nltk
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string

def quitarStopwords_eng(texto):
    ingles = stopwords.words("english")
    texto_limpio = [w.lower() for w in texto if w.lower() not in ingles 
                    and w not in string.punctuation 
                    and w not in ["'s", '|', '--', "''", "``"] ]
    return texto_limpio

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def lematizar(texto):
    texto_lema = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in texto]
    return texto_lema

#Inicializar el Lematizador
lemmatizer = WordNetLemmatizer()

#Corpus de entrenamiento (lista de oraciones tokenizadas para entrenar el modelo.)
corpus = [
    lematizar(quitarStopwords_eng(word_tokenize("The dog plays in the park"))),
    lematizar(quitarStopwords_eng(word_tokenize("The cat sleeps in the house"))),
    lematizar(quitarStopwords_eng(word_tokenize("The dog barks and the cat meows"))),
    lematizar(quitarStopwords_eng(word_tokenize("The cat sleeps in the house and the dog sleeps in the house"))),
    lematizar(quitarStopwords_eng(word_tokenize("The dog barks and the cat meows"))),
    lematizar(quitarStopwords_eng(word_tokenize("The cat meows and the dog barks"))),
    lematizar(quitarStopwords_eng(word_tokenize("The cat and the dog have hair"))),
    lematizar(quitarStopwords_eng(word_tokenize("The dog has four legs and the cat has four legs"))),
    lematizar(quitarStopwords_eng(word_tokenize("The dog is an animal and barks"))),
    lematizar(quitarStopwords_eng(word_tokenize("The cat is an animal and meows"))),
    lematizar(quitarStopwords_eng(word_tokenize("a cat and a dog are animals"))),
    lematizar(quitarStopwords_eng(word_tokenize("An animal is a dog and a cat"))),
    lematizar(quitarStopwords_eng(word_tokenize("An animal is a dog and it barks"))),
    lematizar(quitarStopwords_eng(word_tokenize("An animal is a cat and it meows")))
]
print(corpus)
#Entrenar modelo Word2Vec
model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=3, workers=4)
#sentences=corpus .Este argumento toma un iterable de oraciones (por ejemplo, una lista de listas de palabras) como entrada, que representa el corpus de entrenamiento.
#vector_size=100  .Especifica que cada palabra estará representada por un vector de 100 dimensiones. Esta dimensión captura el significado semántico de la palabra en el espacio vectorial.
#window=5         .Este parámetro define la distancia máxima entre la palabra actual y sus vecinas dentro de una oración. En otras palabras, considera una ventana de 5 palabras a la izquierda y 5 palabras a la derecha de la palabra objetivo durante el entrenamiento.
#min_count=3      .Establece el umbral mínimo de frecuencia de las palabras que se incluirán en el vocabulario. Se ignorarán las palabras que aparezcan menos de 3 veces en el corpus.
#workers=4        .Este argumento especifica la cantidad de subprocesos de trabajo que se utilizarán para el entrenamiento, lo que permite el procesamiento paralelo y potencialmente acelera el proceso de entrenamiento en procesadores de múltiples núcleos.

#Obtener las palabras y sus vectores
words = list(model.wv.index_to_key)  # Lista de palabras del vocabulario
print(words)
vectors = [model.wv[word] for word in words]  # Vectores de las palabras
#Reducir dimensiones con PCA (de 50D a 2D)
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)
print(reduced_vectors)
#Graficar los embeddings
plt.figure(figsize=(10, 8))
for i, word in enumerate(words):
    x, y = reduced_vectors[i]
    plt.scatter(x, y)
    plt.text(x + 0.001, y + 0.001, word, fontsize=8)

plt.title("Visualización de Word Embeddings con PCA")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.grid()
plt.show()