# 📄 Gemini-Powered ATS Resume Analyzer

The **Gemini-Powered ATS Resume Analyzer** leverages Google's Gemini language model to evaluate resumes against job descriptions and provide AI-powered insights. This tool helps job seekers optimize their resumes for better Applicant Tracking System (ATS) compatibility.

---

## 🚀 Features

- 🧠 **Gemini-Powered Analysis**
  - Understands context and intent in both resumes and job descriptions.
- 📊 **ATS Match Percentage**
  - Calculates how well a resume matches a given job description.
- 🔍 **Keyword Insights**
  - Highlights missing or underused keywords from the JD.
- 🛠 **Improvement Suggestions**
  - Suggests natural edits or new projects to boost match score.
- 🧾 **Professional Evaluation**
  - Simulates an HR expert’s review of your resume.

---

## 📂 How It Works

1. Upload your **resume (PDF)**
2. Paste a **job description**
3. Select the analysis type:
   - HR Evaluation
   - ATS Match Percentage
4. View insights, match score, and suggestions for improvement.

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/) – UI Framework
- [Google Generative AI (Gemini)](https://ai.google.dev/) – LLM for content generation
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) – PDF text extraction
- [python-dotenv](https://pypi.org/project/python-dotenv/) – For managing secrets

---

## 🛠 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ats-resume-analyzer.git
cd ats-resume-analyzer
