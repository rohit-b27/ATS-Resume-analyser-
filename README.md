# 📊 ATS Resume Analyzer

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32.1-red.svg)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq%20AI-Llama%203%2070B-green.svg)](https://groq.com/)

An intelligent **ATS (Applicant Tracking System)** resume analyzer powered by **Groq AI** that helps optimize resumes for better job matching.

## ✨ Features

- **🎯 Skills Analysis**: Extract key skills from job descriptions
- **📊 Resume Comparison**: Compare resume with job requirements  
- **📈 Match Percentage**: Get detailed match scores
- **💡 Improvement Suggestions**: Receive actionable recommendations
- **📝 Cover Letter Generation**: Generate tailored cover letters
- **📋 PDF Processing**: Advanced text extraction with PyMuPDF

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up API Key
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the App
```bash
streamlit run app.py
```

## 📖 Usage

1. **Enter job description** in the text area
2. **Upload your resume** (PDF format)
3. **Use the analysis tabs**:
   - Skills Analysis
   - Resume Comparison  
   - Match Score
   - Improvements
   - Cover Letter

## 🔧 Requirements

- Python 3.10+
- Groq API key ([Get one here](https://console.groq.com/))
- PDF resume files

## 📁 Files

- `app.py` - Main application with modern UI
- `main.py` - Advanced edition with comprehensive analysis
- `requirements.txt` - Python dependencies

---

<div align="center">
  <p>Built with ❤️ using <a href="https://streamlit.io/">Streamlit</a> and <a href="https://groq.com/">Groq AI</a></p>
</div> 
