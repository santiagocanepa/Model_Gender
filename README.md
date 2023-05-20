Predicción de Género a partir de Nombres
Este repositorio contiene un proyecto de Python que predice el género de una persona a partir de su nombre.

Descripción del Proyecto
Este proyecto utiliza un modelo de aprendizaje automático basado en el algoritmo de Naive Bayes Multinomial para realizar predicciones del género basándose en un conjunto de nombres previamente clasificados. Se realizó una ampliación de datos para tener un conjunto más grande de nombres para entrenar al modelo. El proyecto también cuenta con un procesador de datos para preparar los datos para el entrenamiento y la predicción.

Estructura de los Archivos
data_augmentation.py: Script para aumentar el conjunto de datos de nombres.
data_classification.py: Script para clasificar los nombres en el conjunto de datos.
model.py: Script que entrena el modelo de aprendizaje automático y realiza predicciones.
processing_data.py: Script que procesa los datos para el modelo.
prueba.py: Script que realiza pruebas de predicciones.
separetor.py: Script que separa los nombres cuando son necesarios.
Cómo Utilizar
Preparar el Entorno
Clonar este repositorio.
Asegurarte de tener Python 3.8 o superior instalado.
Instalar las dependencias de Python necesarias con el comando pip install -r requirements.txt (este archivo deberás crearlo con las dependencias que utilices en tu proyecto).
Uso del Código
El uso básico implicaría ejecutar los scripts en el siguiente orden:

Ejecutar data_augmentation.py para aumentar los datos.
Ejecutar data_classification.py para clasificar los nombres.
Ejecutar processing_data.py para procesar los datos para el modelo.
Ejecutar model.py para entrenar el modelo y hacer una predicción de prueba.
Ejecutar prueba.py para hacer pruebas de predicciones.
Cada uno de estos scripts se ejecuta con el comando python <script-name>.py.

Contribuciones
Las contribuciones a este proyecto son bienvenidas. Para contribuir, por favor:

Haga un "fork" de este repositorio.
Crea tu nueva rama con git checkout -b nombre-de-tu-rama.
Haz tus cambios y confírmalos con git commit -am 'Agregar algunos cambios'.
Empuja a la rama con git push origin nombre-de-tu-rama.
Crea una nueva solicitud de "pull" en GitHub.
Por favor, asegúrate de que tu código pasa todas las pruebas antes de enviar una solicitud de "pull". Si tienes alguna pregunta, no dudes en abrir un "issue" en GitHub.

Contacto
Si tienes alguna pregunta o problema con el código, por favor abre un "issue" en GitHub.

Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo LICENSE para más detalles.

