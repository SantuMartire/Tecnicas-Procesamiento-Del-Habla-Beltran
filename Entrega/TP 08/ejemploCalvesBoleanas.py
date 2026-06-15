import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Descargar recursos necesarios (solo la primera vez)
#nltk.download('punkt')
#nltk.download('stopwords')

# Documentos de ejemplo
documents = {
    "doc1": "La inteligencia artificial es el futuro de la tecnología.",
    "doc2": "El aprendizaje automático es una rama de la inteligencia artificial.",
    "doc3": "El procesamiento del lenguaje natural es un campo de la inteligencia artificial.",
    "doc4": "Los algoritmos de Machine Learning permiten el aprendizaje de datos.",
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

print("\nConsulta: aprendizaje OR machine")
print(boolean_search("aprendizaje OR machine"))  # Debería devolver doc2, doc4

print("\nConsulta: inteligencia NOT aprendizaje")
print(boolean_search("inteligencia NOT aprendizaje"))  # Debería devolver doc1, doc3
