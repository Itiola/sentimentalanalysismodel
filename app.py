import streamlit as st
from transformers import pipeline

# Load the pre-trained model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline("sentiment-analysis", model=model_name)

def analyze_sentiment(text):
  result = classifier(text)
  return result[0]['label'], result[0]['score']

st.title("Sentiment Analyzer")

text_input = st.text_area("Enter your text here")

if st.button("Analyze"):
  if text_input:
    label, score = analyze_sentiment(text_input)
    st.write("Sentiment:", label)
    st.write("Confidence:", score)
  else:
    st.warning("Please enter some text")