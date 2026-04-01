import nltk
from nltk.corpus import gutenberg
from nltk import FreqDist
import matplotlib.pyplot as plt

# 1. Descargar los recursos necesarios (solo la primera vez)
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('punkt_tab') # Necesario en versiones recientes de NLTK

# 2. Cargar Moby Dick desde el corpus de Gutenberg
# NLTK ya lo tiene identificado como 'melville-moby_dick.txt'
palabras = gutenberg.words('melville-moby_dick.txt')

# 3. Calcular la distribución de frecuencia
frecuencia = FreqDist(palabras)

# 4. Mostrar los 20 más comunes
print("20 palabras más comunes en Moby Dick:")
for mc in frecuencia.most_common(20):
    print(mc)

# 5. Graficar
frecuencia.plot(20, show=True)