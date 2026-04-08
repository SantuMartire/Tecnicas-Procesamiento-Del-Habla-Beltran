#Aplicar stop_word, lematizaciòn y aplicar Tf-Idf a un corpus para su analisis.
#Analizarlo
#This software depends on NumPy and Scipy, two Python packages for scientific computing. 
# You must have them installed prior to installing gensim.
#pip install --upgrade gensim
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
#from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
#from gensim.models import Word2Vec
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

#Definir el corpus de texto
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

corpus_final = []

for oracion in corpus:
    resultado = ' '.join(oracion)  # Une los elementos con un espacio
    corpus_final.append(resultado)

print(corpus_final)

#Inicializar el TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus_final)
print("Matriz TF-IDF:")
print(X.toarray())
print("\nVocabulario:")
print(vectorizer.get_feature_names_out())