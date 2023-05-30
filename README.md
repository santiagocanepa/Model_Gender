# Predicción de Género en Base a Nombres - Python

Este proyecto de Python se centra en la predicción del género a partir de nombres utilizando técnicas de aprendizaje automático.

## 📄 Descripción

El proyecto utiliza técnicas de procesamiento de lenguaje natural y un modelo de clasificación Naive Bayes para predecir el género en base a nombres de usuario. Se implementa un proceso de ingesta y clasificación manual de datos para entrenar el modelo, y se utiliza una técnica de aumento de datos para mejorar la robustez del mismo.

## Compatible con instabot o cualquier automatización para redes sociales. 
## 🛠️ Estructura de los Archivos

- `__init__.py`: Este es un archivo requerido para que Python trate los directorios como que contienen paquetes.
- `data_augmentation.py`: Este script se encarga de aumentar el dataset inicial combinando los nombres existentes para crear nuevos nombres.
- `data_classification.py`: En este script se clasifican los nombres en el dataset inicial de forma manual.
- `model.py`: Este archivo contiene el código del modelo de aprendizaje automático, el cual es un clasificador Naive Bayes.
- `processing_data.py`: En este archivo se procesa el dataset para su utilización posterior en el modelo.
- `prueba.py`: Este script utiliza el modelo entrenado para hacer inferencias.
- `separetor.py`: Este script contiene una función para obtener nombres posibles de un nombre de usuario.

## ⚙️ Instalación

1. Clone el repositorio en su máquina local
```bash
git clone https://github.com/santiagocanepa/predictor_genero

Navegue hasta el directorio del proyecto

cd ruta/al/directorio

Instale las dependencias necesarias

pip install -r requirements.txt
Ejecute el script model.py para entrenar el modelo y prueba.py para hacer inferencias.

📃 Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo LICENSE para más detalles.


