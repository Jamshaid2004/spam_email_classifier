# Email Spam Detection App using Logistic Regression + TF-IDF + Streamlit 📧

This project implements a real-time email classification system using **Logistic Regression**, **TF-IDF Vectorization**, and **Streamlit**.
It analyzes the textual content of an email and predicts whether it is **Spam** or **Not Spam (Ham)** with high accuracy.

---

## 🎯 Features

✅ **Logistic Regression Classifier** – Classifies emails efficiently based on trained data.
✅ **TF-IDF Vectorizer** – Converts raw text into numerical feature vectors.
✅ **Text Cleaning Pipeline** – Removes unwanted characters, symbols, and spaces.
✅ **Streamlit Interface** – Provides an interactive and responsive web UI.
✅ **Real-Time Prediction** – Predicts spam or ham instantly after user input.
✅ **Pre-Trained Model** – Loads saved model and vectorizer using joblib.
✅ **Cloud & Local Deployment** – Works seamlessly on Streamlit Cloud or local systems.

---

## ⚙️ How It Works

### 📨 1. Email Input
- The user enters or pastes the content of an email in the provided text box within the Streamlit interface.
  
### 🧹 2. Text Preprocessing

- The input text is cleaned using the following steps:
- Converted to lowercase.
- Removed newline characters (\r\n).
- Removed all special symbols and numbers.
- Replaced multiple spaces with a single space.
- Trimmed unnecessary leading/trailing spaces.

### 🧠 3. Feature Extraction (TF-IDF)
- The cleaned text is transformed into numerical form using a TF-IDF Vectorizer.
- This captures the importance of each word relative to the dataset.
- The same vectorizer used during training (vectorizer.pkl) ensures consistent results.

### 🤖 4. Spam Classification (Logistic Regression)
- The vectorized text is passed to the trained Logistic Regression model (spam_model.pkl).
- The model outputs a binary prediction:
    1 → Spam
    0 → Not Spam

  
### 💬 5. Prediction Output
- Once the Predict button is clicked:
- If the email is spam → 🚨 “This email is SPAM!”
- If the email is not spam → ✅ “This email is NOT spam.”
- The result is displayed instantly on the app interface.

### 📊 6. Model Training (Notebook)

- Model training is performed in the Spam_Email_Classifier.ipynb notebook using the following steps:
- Load dataset (spam_ham_dataset.csv).
- Clean text using the same preprocessing function.\
- Convert text to features using TF-IDF.
- Train the Logistic Regression model.
- Evaluate accuracy on the test set.

### 💾 8. Files Included
- `app.py` → Streamlit application file.
- `spam_model.pkl` → Trained Logistic Regression model.
- `vectorizer.pkl` → TF-IDF vectorizer for text transformation.
- `Spam_Email_Classifier.ipynb` → Notebook for training and testing the model.
- `requirements.txt` → Python dependencies for deployment.
