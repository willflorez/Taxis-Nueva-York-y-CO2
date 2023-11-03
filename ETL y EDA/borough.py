import pandas as pd

# Crear un DataFrame con las columnas "ID" y "Borough"
data = {
    "ID": [1, 2, 3, 4, 5],
    "Borough": ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv("borough.csv", index=False)
