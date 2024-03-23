import os 
import streamlit as st 
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.environ['api_key'])

st. set_page_config(page_title="ATS RESUME ANALYZER")
jd = st.text_input("enter the job description: ", key = "input")
resume = st.file_uploader("upload the resume: ")

def get_response(jd,resume,prompt):
    model = genai.GenerativeModel(model_name="gemini-pro-vision")
    response = model.generate_content([jd,resume[0], prompt])
    return response.text 


def input_pdf_setup(uploaded_file):
    #convert pdf to image
    images = pdf2image.convert_from_bytes(uploaded_file.read())
    
    




