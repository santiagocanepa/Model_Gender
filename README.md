
# 🚀 Model_Gender

🔍 **Project Description**  
This repository contains a gender classifier trained with over 50,000 male and female names. It uses XGBoost and OpenAI embeddings for predictions. You need to connect your OpenAI API, which costs approximately $0.01 per 30,000 names requested, making it practically free.

---

## ⚙️ **Requirements**

To run this project, you need to install the dependencies listed in `requirements.txt`. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

---

## 🚀 **Usage Instructions**

1. **Install the requirements:**  
   Run the `requirements.txt` file in a virtual environment if possible.

2. **Start the local API:**  
   Run `app.py` to launch a local API using Flask, where you can send requests with the words to be predicted:

```bash
python app.py
```

---

## 📂 **Project Structure**

- `app.py`: Launches the local API with Flask and calls `utils.py` to process each request.
- `utils.py`: Receives the words, generates embeddings, and classifies with the `modelWordsPredict.pkl` model to determine if the word is a proper noun or a common noun. If it is a proper noun, it classifies the gender using `modelGenerosPredict.pkl`.

---

## 🗂️ **Included Files**

- `modelWordsPredict.pkl`: Model to classify if the word is a proper noun or a common noun.
- `modelGenerosPredict.pkl`: Model to predict gender in proper nouns.
- `label_encoderWords.pkl`: Label encoder for the word model.
- `label_encoderGeneros.pkl`: Label encoder for the gender model.

---

## 📜 **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

### 📧 **Contact**

If you have questions or suggestions, feel free to open an issue or contact the project maintainer.
