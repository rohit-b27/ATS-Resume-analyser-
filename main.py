import streamlit as st 
import google.generativeai as genai
import os 
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv('api_key'))

def get_gemini_response(jd,prompt):
    model = genai.GenerativeModel('gemini-pro',)
    response = model.generate_content([jd,prompt])
    return response.text


    
def input_pdf_setup(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_number in range(len(reader.pages)):  # Corrected iteration
        page = reader.pages[page_number]
        text += str(page.extract_text())
    return text  

st. set_page_config(page_title="ATS RESUME ANALYZER")
st.header('Best fit application loading....')
jd = st.text_area("enter the job description: ")
resume = st.file_uploader("upload the resume(pdf): ", type=["pdf"])
   
if resume is not None:
    st.write("File uploaded successfully")
else:
    st.write('file not yet uploaded')


prompt1 = """ You are an expert HR with Technical experience in the feilds of Data Science,
    Data Analyst, Machine learning, Generative AI, Data Engineering, DEVOPS, Cloud engineer.  
    You have been provided with the text extracted from resume of an individual in this prompt.
    In the resume, there are 5 different sections, namely education,skills, experience, projects and cirtifications.
    The job description is provided from the user input. so you will be provided with this prompt and jd to process the request. 
    Your task is to extract each and every skill that a job description is looking for,
    that might be tools,frameworks,soft skills,domain knowledge,etc 
    and present it one by one.
    Analyze the simillarity of resume to jd in terms of skills and  
    give out a number, sort of percentage match for the resume to jd. 
    resume:{text}"""

    
   
submit1 = st.button("Get the key words from Job description")

if submit1:
        if resume is not None:
            text = input_pdf_setup(resume)
            result = get_gemini_response(jd,prompt1)
            st.write(result)
    
        
    
    
       
    
submit2 = st.button("Adding Key words to Resume")
prompt2 = """ You are an expert HR with Technical experience in the feilds of Data Science,
    Data Analyst, Machine learning, Generative AI, Data Engineering, DEVOPS, Cloud engineer. 
    you will be provided the Job description in the form of text input and resume in the form of text, 
    Your task is to extract each and every skill that a job description is looking for,
    that might be tools,frameworks,soft skills,domain knowledge,etc and match them with the resume provided,
    if there are any additions needed to be done, let it be known presenting one by one.
    Job description:{jd}
    resume:{file1}"""
if submit2:
        if resume is not None:
            result = get_gemini_response(jd,prompt1)
            st.write(result)
    
    

submit1 = st.button("Percentage Match")
submit1 = st.button("How to improve")
    