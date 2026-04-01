#pip install matplotlib
import nltk

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import FreqDist
corpus = PlaintextCorpusReader(".", 'melville-moby_dick.txt')
frecuencia=FreqDist(corpus.words())

for mc in frecuencia.most_common(20):
    print(mc)

frecuencia.plot(20, show=True)
