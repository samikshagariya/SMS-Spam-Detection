import streamlit as st
import joblib

# Load the trained model and vectorizer
voting = joblib.load('spam_classifier.pkl')
tf_idf_vectorizer = joblib.load('tf_idf_vectorizer.pkl')

def predict_spam(text):
    # Transform the input text using the fitted TF-IDF vectorizer
    transformed_text = tf_idf_vectorizer.transform([text])
    prediction = voting.predict(transformed_text)
    
    return "Spam" if prediction[0] == 1 else "Not Spam"

# Streamlit application
st.title("SMS Spam Classifier")

st.write("Enter SMS Text:")

text = st.text_area("")

if st.button("Predict"):
    if text.strip():
        result = predict_spam(text)
        st.success(f"The message is: {result}")
    else:
        st.warning("Please enter some text!")

# To run the Streamlit application, save this script and run:
# streamlit run streamlit_app.py
