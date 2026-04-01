
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpus = PlaintextCorpusReader(".", 'melville-moby_dick.txt')

print("Total palabras: ", len(corpus.words()))

#for palabra in corpus.words():
#    print(palabra)
