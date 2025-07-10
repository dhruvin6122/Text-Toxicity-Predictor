import streamlit as st
import pickle
import re

# Load model and vectorizer
model = pickle.load(open("models/logistic_model.pkl", "rb"))
vectorizer = pickle.load(open("models/tfidf_vectorizer.pkl", "rb"))

# Labels and their meanings
LABEL_MAP = {
    "toxic": "Mildly Toxic",
    "severe_toxic": "Highly Abusive",
    "obscene": "Obscene Language",
    "threat": "Threatening Content",
    "insult": "Contains Insults",
    "identity_hate": "Hate Speech"
}

LABELS = list(LABEL_MAP.keys())

# Clean function
def clean(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|@\w+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.strip()

# Prediction + interpretation function
def predict_and_interpret(text):
    cleaned = clean(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]

    result_lines = []
    any_flag = False
    for label, val in zip(LABELS, pred):
        if val == 1:
            result_lines.append(f"✅ {LABEL_MAP[label]}")
            any_flag = True

    if not any_flag:
        result_lines.append("✅ Not Toxic or Offensive")

    return result_lines

# Streamlit UI
st.set_page_config(page_title="Toxic Comment Detector", layout="centered")
st.title("🧠 Toxic Comment Detector (ML Powered)")
st.write("Paste a comment below to detect if it's toxic, insulting, obscene, threatening, or hateful.")

user_input = st.text_area("💬 Enter a comment here:")

if st.button("Analyze"):
    if user_input.strip():
        results = predict_and_interpret(user_input)
        st.subheader("🔍 Result:")
        for line in results:
            st.write(line)
    else:
        st.warning("Please enter a comment to analyze.")
