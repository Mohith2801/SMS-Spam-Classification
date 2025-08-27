import streamlit as st
import pickle

# Load model and vectorizer
with open('spam_classifier_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('tfidf_vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

st.title("SMS Spam Classifier")

sms = st.text_input("Enter SMS message:")

if st.button("Classify"):
    if sms.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Preprocess input if needed (lowercase, etc.)
        sms_processed = sms.lower()
        features = vectorizer.transform([sms_processed])
        prediction = model.predict(features)
        st.write(f"Raw prediction: {prediction[0]}")  # Debug output
        if prediction[0] == 0:
            st.success("Ham mail")
        else:
            st.error("Spam mail")