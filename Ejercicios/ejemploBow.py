from sklearn.feature_extraction.text import CountVectorizer
#pip install scikit-learn
# Definir el corpus de texto
corpus = [
    "El perro ladra",
    "El gato maulla",
    "El perro y el gato juegan juntos"
]

# Inicializar el CountVectorizer (BoW)
vectorizer = CountVectorizer()

# Aplicar BoW (tokenización + conteo de palabras)
X = vectorizer.fit_transform(corpus)

# Mostrar la matriz BoW
print("Matriz BoW (frecuencia de palabras):")
print(X.toarray())

# Mostrar las palabras únicas (vocabulario)
print("\nVocabulario:")
print(vectorizer.get_feature_names_out())
