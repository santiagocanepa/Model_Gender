import pandas as pd


df = pd.read_csv("classified_names.csv")


# Crear un nuevo DataFrame vacío para almacenar los resultados
resultado = pd.DataFrame(columns=["nombre", "gender"])

# Recorrer cada fila del conjunto de datos original
for index, row in df.iterrows():
    # Comprobar si hay dos nombres en la columna "nombre"
    if " " in row["nombre"]:
        # Separar los nombres
        nombres = row["nombre"].split(" ")
        
        # Añadir cada nombre separado al nuevo DataFrame con el mismo género
        for nombre in nombres:
            resultado = resultado.append({"nombre": nombre, "gender": row["gender"]}, ignore_index=True)
    else:
        # Si no hay dos nombres, simplemente añadir la fila al nuevo DataFrame
        resultado = resultado.append(row, ignore_index=True)

# Guardar el DataFrame modificado en un archivo csv
resultado.to_csv("classified_names_augmentation.csv", index=False)
