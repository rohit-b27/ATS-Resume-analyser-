import os 
import streamlit as st 
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.environ['api_key'])


def get_response(jd,resume,prompt):
    model = genai.GenerativeModel(model_name="gemini-pro-vision")
    response = model.generate_content([jd,resume[0], prompt])
    return response.text 


def input_pdf_setup(uploaded_file):
    #convert pdf to image
    if uploaded_file is not None:
       images = pdf2image.convert_from_bytes(uploaded_file.read())
    
       content = images[0]
       content_byte_arr = io.BytesIO()
       content.save(content_byte_arr,format = 'JPEG')
       bytes_data = content.getvalue()
       pdf_parts = [
                {
                    "mime_type": "image/jpeg", 
                    "data": base64.b64encode(bytes_data).decode()
                }
            ]
       return pdf_parts
   
    
   
st. set_page_config(page_title="ATS RESUME ANALYZER")
jd = st.text_input("enter the job description: ", key = "input")
resume = st.file_uploader("upload the resume(pdf): ", type=["pdf"])
   
if resume is not None:
    st.write("File uploaded successfully")

file1 = input_pdf_setup(resume)
    
   
submit1 = st.button("Get the key words from Job description")
if submit1:
    prompt1 = """ You are an expert HR with Technical experience in the feilds of Data Science,
    Data Analyst, Machine learning, Generative AI, Data Engineering, DEVOPS, Cloud engineer. 
    you will be provided the Job description in the form of text input, 
    Your task is to extract the key Techincal skills that a job description is looking for, 
    and present it one by one. """
    result = get_response(jd,file1,prompt1)
    st.write(result)
       
    
submit2 = st.button("Adding Key words to Resume")
if submit2:
    prompt2 = """ You are an expert HR with Technical experience in the feilds of Data Science,
    Data Analyst, Machine learning, Generative AI, Data Engineering, DEVOPS, Cloud engineer. 
    you will be provided the Job description in the form of text input and resume in the form of document, 
    Your task is to extract the key Techincal skills that a job description is looking for and match them with the resume provided,
    if there are any additions to be done, let it be known presenting one by one. """
    result = get_response(jd,file1,prompt2)
    st.write(result)

submit1 = st.button("Percentage Match")
submit1 = st.button("How to improve")
   