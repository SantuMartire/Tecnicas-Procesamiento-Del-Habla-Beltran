#pip install pandas

import pandas as pd

#df = pd.DataFrame({"Animal": ["perro", "gato", "pez", "perro", "pez"]})
df = pd.DataFrame({"Oracion": ["El",  "perro" , "es",  "negro","El",  "perro", "ladra"]})

# Aplicar One-Hot Encoding con Pandas
one_hot_df = pd.get_dummies(df, columns=["Oracion"])

print(one_hot_df)