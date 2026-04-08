from sklearn.feature_extraction.text import TfidfVectorizer

#Definir el corpus de texto
corpus = [
    "El perro ladra",
    "El gato maulla",
    "El perro y el gato juegan juntos"
]

#Inicializar el TfidfVectorizer
vectorizer = TfidfVectorizer()

#Aplicar TF-IDF al corpus
X = vectorizer.fit_transform(corpus)

#Mostrar la matriz TF-IDF
print("Matriz TF-IDF:")
print(X.toarray())

#Mostrar el vocabulario generado
print("\nVocabulario:")
print(vectorizer.get_feature_names_out())