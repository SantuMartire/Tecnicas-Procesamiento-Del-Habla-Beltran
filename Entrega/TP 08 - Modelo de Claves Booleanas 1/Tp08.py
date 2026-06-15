import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Consigna 1:
#Crea un programa en Python que permita al usuario realizar búsquedas booleanas (AND, OR, NOT) en un
#conjunto de documentos utilizando NLTK.

#-Se tienen 5 documentos con información sobre inteligencia artificial y aprendizaje automático.
#   "doc1": "La inteligencia artificial está revolucionando la tecnología.",
#   "doc2": "El aprendizaje automático es clave en la inteligencia artificial.",
#   "doc3": "Procesamiento del lenguaje natural y redes neuronales.",
#   "doc4": "Las redes neuronales son fundamentales en deep learning.",
#   "doc5": "El futuro de la IA está en el aprendizaje profundo."

#1)-Implementa una función que tokenice y limpie los documentos.
#2) -Crea un índice invertido (asocia cada palabra clave a los documentos en los que aparece)
#3) -Permite que el usuario ingrese una consulta booleana y devuelva los documentos relevantes.


documents = {
    "doc1": "La inteligencia artificial está revolucionando la tecnología.",
    "doc2": "El aprendizaje automático es clave en la inteligencia artificial.",
    "doc3": "Procesamiento del lenguaje natural y redes neuronales.",
    "doc4": "Las redes neuronales son fundamentales en deep learning.",
    "doc5": "El futuro de la IA está en el aprendizaje profundo."
}

# Preprocesamiento: Tokenización y eliminación de stopwords
stop_words = set(stopwords.words('spanish'))

def preprocess(text):
    tokens = word_tokenize(text.lower())  # Convertir a minúsculas y tokenizar
    return set([word for word in tokens if word.isalnum() and word not in stop_words])

# Índice invertido (palabra clave → documentos donde aparece)
index = {}
for doc_id, text in documents.items():
    words = preprocess(text)
    for word in words:
        if word not in index:
            index[word] = set()
        index[word].add(doc_id)

# Función para búsqueda booleana
def boolean_search(query):
    terms = query.split()  # Separar los términos
    result_set = set(documents.keys())  # Comenzamos con todos los documentos

    i = 0
    while i < len(terms):
        term = terms[i]
        if term == "AND":
            i += 1
            result_set &= index.get(terms[i], set())  # Intersección (AND)
        elif term == "OR":
            i += 1
            result_set |= index.get(terms[i], set())  # Unión (OR)
        elif term == "NOT":
            i += 1
            result_set -= index.get(terms[i], set())  # Diferencia (NOT)
        else:
            result_set &= index.get(term, set())  # Primera palabra
        i += 1
    
    return result_set

# Ejemplos de consulta

print ("Índice invertido:")
for word, docs in index.items():
    print(f"{word}: {docs}")

print("\nConsulta: inteligencia AND artificial")
print(boolean_search("inteligencia AND artificial"))  # Debería devolver doc1, doc2, doc3

print("\nConsulta: redes OR aprendizaje")
print(boolean_search("redes OR aprendizaje"))  # Debería devolver doc2, doc4

print("\nConsulta: inteligencia NOT automático")
print(boolean_search("inteligencia NOT automático"))  # Debería devolver doc1, doc3
