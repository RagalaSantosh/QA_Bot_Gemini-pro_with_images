import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")


model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)

    return response.text


st.set_page_config(page_title = "Gemini Image Reader")

st.header("Gemini Image Reader")

input = st.text_input("Input Prompt: ", key = "input")

uploaded_image = st.file_uploader("Upload your image here", type=['png', 'jpeg', 'jpg'])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption = "Uploaded Image", use_column_width = True)

submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_response(input, image)

    st.subheader("The Response is")
    st.write(response)
