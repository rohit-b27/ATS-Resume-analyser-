import os 
import streamlit as st 
import fitz  # PyMuPDF
import pandas as pd
import numpy as np
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

# Page configuration
st.set_page_config(
    page_title="ATS Resume Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_groq_response(jd, resume_text, prompt):
    """Get response from Groq API"""
    try:
        full_prompt = f"Job Description: {jd}\n\nResume Text: {resume_text}\n\nPrompt: {prompt}"
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            model="llama3-70b-8192",
            temperature=0.7,
            max_tokens=2048
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def extract_text_from_pdf(uploaded_file):
    """Extract text from PDF using PyMuPDF"""
    if uploaded_file is not None:
        try:
            # Read the PDF file
            pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            text = ""
            
            # Extract text from all pages
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                text += page.get_text()
            
            pdf_document.close()
            return text.strip()
        except Exception as e:
            st.error(f"Error reading PDF: {str(e)}")
            return ""
    return ""

def analyze_skills(jd_text):
    """Analyze job description to extract required skills"""
    prompt = """You are an expert HR with Technical experience in the fields of Data Science,
    Data Analyst, Machine learning, Generative AI, Data Engineering, DEVOPS, Cloud engineer. 
    Extract the key Technical skills, tools, frameworks, and requirements from the job description.
    Present them in a clear, organized format with categories like:
    - Programming Languages
    - Frameworks & Libraries
    - Tools & Technologies
    - Soft Skills
    - Experience Requirements"""
    
    return get_groq_response(jd_text, "", prompt)

def compare_resume_jd(jd_text, resume_text):
    """Compare resume with job description"""
    prompt = """You are an expert HR with Technical experience in the fields of Data Science,
    Data Analyst, Machine learning, Generative AI, Data Engineering, DEVOPS, Cloud engineer. 
    Compare the resume with the job description and provide:
    1. Skills present in resume that match job requirements
    2. Missing skills that should be added to resume
    3. Specific recommendations for improvement
    4. Overall assessment of fit for the position"""
    
    return get_groq_response(jd_text, resume_text, prompt)

def calculate_match_percentage(jd_text, resume_text):
    """Calculate percentage match between resume and job description"""
    prompt = """You are an expert HR with Technical experience in the fields of Data Science,
    Data Analyst, Machine learning, Generative AI, Data Engineering, DEVOPS, Cloud engineer. 
    Analyze the similarity of resume to job description and provide:
    1. A percentage match score (0-100%)
    2. Detailed reasoning for the score
    3. Key strengths of the resume
    4. Areas that need improvement
    Be specific and provide actionable insights."""
    
    return get_groq_response(jd_text, resume_text, prompt)

def generate_improvement_suggestions(jd_text, resume_text):
    """Generate improvement suggestions for resume"""
    prompt = """You are an expert HR with Technical experience in the fields of Data Science,
    Data Analyst, Machine learning, Generative AI, Data Engineering, DEVOPS, Cloud engineer. 
    Based on the job description and resume, provide specific recommendations on how to improve the resume
    to better match the job requirements. Focus on actionable suggestions for:
    1. Skills to add or emphasize
    2. Experience descriptions to improve
    3. Keywords to include
    4. Overall resume structure improvements
    5. Specific phrases or achievements to highlight"""
    
    return get_groq_response(jd_text, resume_text, prompt)

def generate_cover_letter(jd_text, resume_text):
    """Generate a cover letter based on resume and job description"""
    prompt = """You are an expert HR with Technical experience in the fields of Data Science,
    Data Analyst, Machine learning, Generative AI, Data Engineering, DEVOPS, Cloud engineer. 
    Based on the job description and resume provided, generate a compelling cover letter that:
    1. Highlights the candidate's relevant experience and skills
    2. Addresses the specific requirements mentioned in the job description
    3. Shows enthusiasm for the position and company
    4. Is professional, concise, and well-structured
    5. Uses specific examples from the resume
    Make it personalized and impactful."""
    
    return get_groq_response(jd_text, resume_text, prompt)

# Main UI
st.title("📊 ATS Resume Analyzer")
st.markdown("---")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("Powered by Groq AI - Llama 3 70B")
    
    # API Key status
    if os.environ.get('GROQ_API_KEY'):
        st.success("✅ API Key Configured")
    else:
        st.error("❌ API Key Missing")
        st.info("Add GROQ_API_KEY to your .env file")

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Job Description")
    jd_text = st.text_area(
        "Enter the job description:",
        height=200,
        placeholder="Paste the complete job description here..."
    )

with col2:
    st.subheader("📄 Resume Upload")
    uploaded_file = st.file_uploader(
        "Upload your resume (PDF):",
        type=["pdf"],
        help="Upload a PDF resume to analyze"
    )

# Process uploaded file
resume_text = ""
if uploaded_file is not None:
    with st.spinner("Extracting text from PDF..."):
        resume_text = extract_text_from_pdf(uploaded_file)
    
    if resume_text:
        st.success("✅ Resume text extracted successfully!")
        with st.expander("📋 View extracted resume text"):
            st.text(resume_text[:1000] + "..." if len(resume_text) > 1000 else resume_text)
    else:
        st.error("❌ Could not extract text from PDF. Please try a different file.")

# Analysis buttons
st.markdown("---")
st.subheader("🔍 Analysis Tools")

# Create tabs for different analyses
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 Skills Analysis", 
    "📊 Resume Comparison", 
    "📈 Match Score", 
    "💡 Improvements", 
    "📝 Cover Letter"
])

with tab1:
    st.subheader("🎯 Extract Required Skills")
    if st.button("Analyze Job Description", type="primary"):
        if jd_text:
            with st.spinner("Analyzing job description..."):
                result = analyze_skills(jd_text)
                st.markdown(result)
        else:
            st.warning("Please enter a job description first.")

with tab2:
    st.subheader("📊 Compare Resume with Job Description")
    if st.button("Compare Resume", type="primary"):
        if jd_text and resume_text:
            with st.spinner("Comparing resume with job description..."):
                result = compare_resume_jd(jd_text, resume_text)
                st.markdown(result)
        else:
            st.warning("Please provide both job description and resume.")

with tab3:
    st.subheader("📈 Calculate Match Percentage")
    if st.button("Calculate Match", type="primary"):
        if jd_text and resume_text:
            with st.spinner("Calculating match percentage..."):
                result = calculate_match_percentage(jd_text, resume_text)
                st.markdown(result)
        else:
            st.warning("Please provide both job description and resume.")

with tab4:
    st.subheader("💡 Improvement Suggestions")
    if st.button("Get Suggestions", type="primary"):
        if jd_text and resume_text:
            with st.spinner("Generating improvement suggestions..."):
                result = generate_improvement_suggestions(jd_text, resume_text)
                st.markdown(result)
        else:
            st.warning("Please provide both job description and resume.")

with tab5:
    st.subheader("📝 Generate Cover Letter")
    if st.button("Generate Cover Letter", type="primary"):
        if jd_text and resume_text:
            with st.spinner("Generating cover letter..."):
                result = generate_cover_letter(jd_text, resume_text)
                st.markdown(result)
        else:
            st.warning("Please provide both job description and resume.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with ❤️ using Streamlit and Groq AI</p>
</div>
""", unsafe_allow_html=True)
   