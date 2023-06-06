# Gender Prediction Based on Names - Python
This Python project focuses on gender prediction from names using machine learning techniques.

# 📄 Description**
The project utilizes natural language processing techniques and a Naive Bayes classification model to predict gender based on usernames. It implements a data ingestion and manual classification process to train the model, and uses a data augmentation technique to enhance its robustness.

Compatible with instabot or any social media automation.

# 🛠️ File Structure
**init.py**: This is a required file for Python to treat directories as containing packages.
**data_augmentation.py**: This script is responsible for augmenting the initial dataset by combining existing names to create new ones.
**data_classification.py**: In this script, the names in the initial dataset are manually classified.
**model.py**: This file contains the code for the machine learning model, which is a Naive Bayes classifier.
**processing_data.py**: In this file, the dataset is processed for subsequent use in the model.
**test.py**: This script uses the trained model to make inferences.
**separator.py**: This script contains a function to obtain possible names from a username.

# ⚙️ Installation
Clone the repository on your local machine


**git clone https://github.com/santiagocanepa/gender_predictor**
Navigate to the project directory

cd path/to/directory
Install the necessary dependencies

pip install -r requirements.txt
Run the model.py script to train the model and test.py to make inferences.

# 📃 License
This project is licensed under the terms of the MIT license. See the LICENSE file for more details.

