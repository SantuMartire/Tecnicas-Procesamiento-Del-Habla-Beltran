import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
#nltk.download('averaged_perceptron_tagger_eng') #por unica vez
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)
#Inicializar el Lematizador
lemmatizer = WordNetLemmatizer()
# Definir la oración a lemmatizar
oracion = "The striped bats are hanging on their feet for best"

# Tokenizar la oración en palabras
word_list = nltk.word_tokenize(oracion)
print(word_list)

#Lematizar la oración con el POS apropiado
for w in word_list:
    #print(w)
    print(lemmatizer.lemmatize(w, get_wordnet_pos(w)))