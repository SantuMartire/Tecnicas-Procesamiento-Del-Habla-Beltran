import nltk
from nltk.corpus import gutenberg
# para cada libro que está disponible en el objeto gutenberg
for libro in gutenberg.fileids():
    caracteres = len(gutenberg.raw(libro))
    palabras = len(gutenberg.words(libro))
    oraciones = len(gutenberg.sents(libro))
    parrafos = len(gutenberg.paras(libro))
    print(
        libro[:-4],
        "\t",
        round(caracteres / palabras, 2),
        "\t",
        round(palabras / oraciones, 2),
        "\t",
        round(oraciones / parrafos, 2),
    )