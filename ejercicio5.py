import nltk
nltk.download('punkt_tab')

from nltk.corpus import gutenberg
# cargo la versión de Alicia segmentada en palabras
alice_words = gutenberg.words("carroll-alice.txt")
print("PALABRAS")
print(alice_words[:20])  # imprimo las primeros 20 palabras
print(len(alice_words))
print("-"*70)
# cargo la versión de Alicia segmentada en oraciones
alice_sents = gutenberg.sents("carroll-alice.txt")
print("ORACIONES")
print("Alice tiene", len(alice_sents), "oraciones")
print(alice_sents[2:5])  # imprimo la tercera, cuarta y quinta oración
print("-"*70)
# cargo la versión de Alicia segmentada en párrafos
alice_paras = gutenberg.paras("carroll-alice.txt")
print("PARRAFOS")
print("Alice tiene", len(alice_paras), "párrafos")
# imprimo los cinco primeros
for para in alice_paras[:5]:
    print(para)
    print("\n", "-" * 75, "\n")