import streamlit as st
import joblib
import re

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\r\n', ' ', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

st.title("📧 Email Spam Detection App")
st.write("Enter an email below and find out if it’s spam or not!")

user_input = st.text_area("Paste your email here:", height=300)

if st.button("Predict"):
    cleaned = clean_text(user_input)
    vectorized = vectorizer.transform([cleaned])
    result = model.predict(vectorized)[0]
    if result == 1:
        st.error("🚨 This email is SPAM!")
    else:
        st.success("✅ This email is NOT spam.")
