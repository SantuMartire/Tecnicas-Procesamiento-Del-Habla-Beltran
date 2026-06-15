#Modelo de Espacio Vectorial
#Consigna 1:

#Crea un programa en Python que busque las similitudes en un conjunto de documentos con modelo de
#espacio vectorial utilizando sklearn.

#Pasos a seguir:

#-Se tienen 3 documentos con información sobre animales.
#   "doc1": "El veloz zorro marrón salta sobre el perro perezoso.",
#   "doc2": "Un perro marrón persiguió al zorro.",
#   "doc3": "El perro es perezoso.",

#-Convertir documentos a vectores usando TF-IDF.

#-Calcular la similitud del coseno entre los documentos.

#-Graficar la matriz de similitud.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

documents = {
    "doc1": "El veloz zorro marrón salta sobre el perro perezoso.",
    "doc2": "Un perro marrón persiguió al zorro.",
    "doc3": "El perro es perezoso."
}

#Convertir documentos a vectores usando TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

#Calcular la similitud del coseno entre los documentos
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

print("Matriz de Similitud del Coseno:")
print(cosine_sim)

# Graficar la matriz de similitud
plt.figure(figsize=(8,6))
sns.heatmap(cosine_sim, annot=True, cmap="Blues", xticklabels=[f"Doc{i+1}" for i in range(len(documents))],
yticklabels=[f"Doc{i+1}" for i in range(len(documents))])
plt.title("Matriz de Similitud del Coseno")
plt.show()