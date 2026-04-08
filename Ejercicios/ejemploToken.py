import tiktoken

# Texto que deseas tokenizar
text = "El verdadero peligro no es que las computadoras empiecen a pensar como hombres, sino que los hombres empiecen a pensar como computadoras. Sydney G. Harris"

# Escoge el modelo de GPT-3 para el que deseas tokenizar (por ejemplo, 'gpt-3.5-turbo')
encoder = tiktoken.get_encoding("gpt2")  # GPT-3 usa el tokenizador de GPT-2

# Tokenizar el texto
tokens = encoder.encode(text)

# Imprimir los tokens y el número de tokens
print("Tokens:", tokens)
print("Número de tokens:", len(tokens))


