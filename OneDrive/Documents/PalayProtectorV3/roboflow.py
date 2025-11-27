# === ROBLOW STREAMLIT SAFE VERSION ===
import streamlit as st
import requests
from PIL import Image

API_KEY = "Jr5X1FoeyfnsQjX4bM65"
MODEL_ID = "palay-protector/1"

st.title("🌾 Palay Protector")

def detect_disease(image_file):
    url = f"https://detect.roboflow.com/{MODEL_ID}"
    params = {"api_key": API_KEY}
    files = {"file": image_file}
    response = requests.post(url, params=params, files=files)
    return response.json()

uploaded_file = st.file_uploader("Upload rice leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    if st.button("Detect"):
        result = detect_disease(uploaded_file)
        st.json(result)
