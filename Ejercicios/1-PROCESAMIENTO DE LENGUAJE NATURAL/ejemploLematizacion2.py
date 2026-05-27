import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
#nltk.download('averaged_perceptron_tagger_eng') #por unica vez

lemmatizer = WordNetLemmatizer()
# Definir la oración a lemmatizar
oracion = "The striped bats are hanging on their feet for best"

# Tokenizar la oración en palabras
word_list = nltk.word_tokenize(oracion)
print(word_list)

print(nltk.pos_tag(word_list))
