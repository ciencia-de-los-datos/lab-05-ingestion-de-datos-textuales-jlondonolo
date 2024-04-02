import os
import pandas as pd
import zipfile

# Descomprimir el archivo data.zip en la carpeta raiz
with zipfile.ZipFile("data.zip", "r") as zip_ref:
    zip_ref.extractall()


# Función para leer los archivos de texto y crear el DataFrame
def create_dataset(data_dir):
    data = []
    for sentiment in os.listdir(data_dir):  #
        sentiment_dir = os.path.join(data_dir, sentiment)

        # Ignorar archivos ocultos, como ._.DS_Store en macOS
        if not sentiment.startswith("."):
            for filename in os.listdir(sentiment_dir):
                filepath = os.path.join(sentiment_dir, filename)

                # Ignorar archivos ocultos
                if not filename.startswith("."):
                    with open(filepath, "r", encoding="utf-8") as file:
                        phrase = file.read().strip()
                    data.append({"phrase": phrase, "sentiment": sentiment})

    return pd.DataFrame(data)


# Crear csv
train_data = create_dataset("train")
train_data.to_csv("train_dataset.csv", index=False)

test_data = create_dataset("test")
test_data.to_csv("test_dataset.csv", index=False)
