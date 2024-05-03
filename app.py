import streamlit as st 
import PyPDF2 as pdf 
import os
from dotenv import load_dotenv
import google.generativeai as genai 

# Load environment variables
load_dotenv()

# Configure API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Function to extract text from uploaded PDF resume
def input_pdf_text(uploaded_file):
    text = ""
    reader = pdf.PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text()
    return text 

# Function to get the three most important responsibilities from job description
def get_important_responsibilities(jd):
    input_prompt = f"Analyze job description to identify the 3 most important responsibilities: {jd}"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    responsibilities = response.text.split('\n')[:3]
    return responsibilities

# Function to tailor the resume based on extracted responsibilities
def tailor_resume(jd_responsibilities, company_name, resume):
    input_prompt = f"""You are an expert resume writer. You are tasked with tailoring a resume for a position at {company_name}, Here are the following 3 key responsibilities: {', '.join(jd_responsibilities)}. Here's the resume: {resume_text}."""
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    return response.text

# Streamlit app frontend
st.title("Smart ATS Resume Tailor - Resume Assistant")
st.text("Craft a targeted resume for each application!")

# Input fields
jd = st.text_area("Paste Job Description Here")
role = st.text_input("Enter Role")
company_name = st.text_input("Enter Company Name")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf", help="Please upload your resume in PDF format")
submit = st.button("Submit")

# Handling submission
if submit:
    if jd and company_name and uploaded_file:
        resume_text = input_pdf_text(uploaded_file)
        jd_responsibilities = get_important_responsibilities(jd)

        #Tailor Resume
        tailored_resume = tailor_resume(jd_responsibilities, company_name, resume_text)

        st.subheader("Top 3 Responsibilities:")
        st.write("\n".join(jd_responsibilities))

        st.subheader("Tailored Resume for" + role + company_name )
        st.write(tailored_resume)
    else:
        st.error("Please fill in all fields and upload a resume.")
