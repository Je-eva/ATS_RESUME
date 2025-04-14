Sure! Here's the complete `README.md` content in **Markdown code** format:

```markdown
# 💼 Smart ATS – Resume Evaluator using Google Gemini API 🚀

Welcome to **Smart ATS**, a lightweight yet powerful resume evaluation tool that leverages **Google's Gemini LLM (Large Language Model)** and **Streamlit** to help job seekers improve their resumes based on job descriptions.

This was one of my **initial projects** in AI, created to explore how **LLMs can be used for real-world automation**, particularly in the hiring process. It gave me hands-on experience with **prompt engineering**, **LLM APIs**, and working with **PDF documents and Streamlit UI**.

---

## 🧠 What It Does

Smart ATS simulates the behavior of an **Applicant Tracking System (ATS)**, but instead of relying on fixed rule-based keyword matching, it uses the power of **Generative AI** through **Gemini 1.5 Pro** to intelligently:

- Parse and read resume PDFs
- Accept a job description input
- Analyze resume vs job description
- Output:
  - **Match percentage**
  - **Missing keywords**
  - **Profile summary**

---

## 📁 Features

- 🔍 **AI-Driven Resume Scanning**  
  Evaluates resumes using natural language understanding.

- 📝 **Dynamic Job Description Matching**  
  Paste any JD, and the AI matches it with the resume content.

- 📄 **PDF File Support**  
  Extracts and processes resume text from PDF format.

- 💬 **Smart Feedback**  
  Helps users improve their resume with clear suggestions and insights.

---

## 🚀 How It Works – Code Flow

```python
1. User uploads a PDF resume and enters a Job Description (JD)
2. The PDF is read using PyPDF2 and converted into raw text
3. A formatted prompt is created combining the resume text and the JD
4. This prompt is passed to Google's Gemini 1.5 Pro model via API
5. The AI responds with:
   - Resume to JD match %
   - Missing keywords
   - A short profile summary
6. The response is displayed beautifully in Streamlit
```

---

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Streamlit** – For building the front-end web UI
- **PyPDF2** – PDF file reading and text extraction
- **Google Generative AI SDK** – To access Gemini models
- **dotenv** – For managing API keys securely

---

## 📸 Screenshot

*(You can add a screenshot of your Streamlit app here for visual context)*

---

## 📦 Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/smart-ats-gemini.git
cd smart-ats-gemini
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Google API key:
```bash
GOOGLE_API_KEY=your_key_here
```

4. Run the app:
```bash
streamlit run app.py
```

---

## 🤝 Special Thanks
**Thanks to [Kish Naik](https://www.youtube.com/@krishnaik06)** for providing open access and examples around **Google's Gemini API**, which inspired me to start exploring real-world applications of LLMs.

---

## 🧠 Final Thoughts

This is a **basic yet impactful project** for those stepping into the field of Generative AI. It lays a strong foundation in working with APIs, PDFs, prompts, and AI-driven logic. It also showcases how AI can enhance hiring tools by making resume filtering smarter and more meaningful.

---
🔗 *Feel free to fork, improve, or customize it for your needs!*
```
