#pip install gensim
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

def quitarStopwords_esp(texto):
    espaniol = stopwords.words("spanish")
    texto_limpio = [w.lower() for w in texto if w.lower() not in espaniol 
                    and w not in string.punctuation
                    and w not in ["El", 'el', 'y', "la", "en"]]
    return texto_limpio

#Corpus de entrenamiento (lista de oraciones tokenizadas para entrenar el modelo.)
corpus = [
    quitarStopwords_esp(word_tokenize("El perro juega en el parque")),
    quitarStopwords_esp(word_tokenize("El gato duerme en la casa")),
    quitarStopwords_esp(word_tokenize("El perro ladra y el gato maulla")),
    quitarStopwords_esp(word_tokenize("El gato duerme en la casa y el perro duerme en la casa")),
    quitarStopwords_esp(word_tokenize("El perro ladra y el gato maulla")),
    quitarStopwords_esp(word_tokenize("El gato y el perro tienen pelos")),
    quitarStopwords_esp(word_tokenize("El perro tiene cuatro patas y el gato tiene cuatro patas"))
]

#Entrenar el modelo Word2Vec -  Entrena un modelo de Word Embeddings basado en contexto.
#vector_size=100 → Cada palabra se representa con un vector de 100 dimensiones.
#window=5 → Considera hasta 5 palabras de contexto en cada lado.
#min_count=1 -> Palabras que aparecen al menos 1 vez serán incluidas en el modelo.
#workers=4 -> Usa 4 núcleos del procesador para entrenar más rápido.
model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=5, workers=4)

#vector_perro = model.wv["perro"]
#vector_gato = model.wv["gato"]
#vector_juega = model.wv["casa"]

print("-"*10)
print("Similitud entre perro y gato : ",model.wv.similarity("perro","gato"))
print("-"*10)
#Encontrar palabras similares a "gato"
print("Top de palabras similares a gato: ", model.wv.most_similar("gato"))
#"Perro" y "gato" son similares porque aparecen en contextos parecidos.
#Los valores están entre -1 y 1 (1 significa "idéntico", 0 "sin relación", -1 "opuesto").
