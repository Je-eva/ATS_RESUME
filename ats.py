import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text):
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
        response = model.generate_content(input_text)
        
        logging.debug(f"Response from model: {response}")
        
        return response.text
    except Exception as e:
        logging.error(f"Error while calling the Gemini model: {e}")
        return f"An error occurred: {e}"

def inp_pdf_text(uploaded_file):
    try:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()  # Extracting text from all page
        return text
    except Exception as e:
        logging.error(f"Error reading PDF: {e}")
        return "Error reading PDF"

# Enter the prompt as req
input_prompt = """
Act like an experienced ATS (Application Tracking System) with a deep understanding of the tech field. Your task is to evaluate the resume based on the given job description. 
Resume: {text}
Description: {jd}

Please respond with the JD match percentage, the missing keywords, and a profile summary.
"""

#  UI
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = inp_pdf_text(uploaded_file) 
        if text != "Error reading PDF":
            input_text = input_prompt.format(text=text, jd=jd)  #frmat input text with resume and JD
            response = get_gemini_response(input_text)  # Get response from model
            st.subheader(response)  # Display response
        else:
            st.error("Error reading the uploaded PDF.")
