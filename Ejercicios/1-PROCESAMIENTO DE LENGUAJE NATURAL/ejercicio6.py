import nltk
from nltk.corpus import gutenberg
alice = gutenberg.raw("carroll-alice.txt")
alice_words = gutenberg.words("carroll-alice.txt")
alice_sents = gutenberg.sents("carroll-alice.txt")
alice_paras = gutenberg.paras("carroll-alice.txt")
print(len(alice), "caracteres")
print(len(alice_words), "palabras")
print(len(alice_sents), "oraciones")
print(len(alice_paras), "párrafos")