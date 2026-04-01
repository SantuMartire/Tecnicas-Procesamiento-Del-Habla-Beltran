import nltk

'''
from nltk.corpus import gutenberg
nltk.download('gutenberg')
libros=gutenberg.fileids() #cargar el catalogo de libros completo
'''
from nltk.corpus import inaugural
nltk.download('inaugural')
libros=inaugural.fileids() #cargar el catalogo de libros completo


for i in libros:
    print(i)

'''
print(" ")

for i in range(len(libros)):
    print(i, libros[i])
'''