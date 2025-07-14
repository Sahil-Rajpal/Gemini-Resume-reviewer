# Gemini-Powered-ATS-Resume-Analyzer 📄

This project provides a user-friendly Streamlit interface to analyze resumes using Google's Gemini language model. It evaluates resumes against job descriptions and returns match percentages, missing keywords, and actionable suggestions for improvement — optimized for Applicant Tracking Systems (ATS).

## Prerequisites

- Python 3.7 or later  
- `streamlit` package  
- `dotenv` package  
- Google AI API key for Gemini model  
- `PyMuPDF` (for reading PDF resumes)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/ats-resume-analyzer.git
    cd ats-resume-analyzer
    ```

2. Create a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # Windows: env\Scripts\activate.bat
    # You can use a conda environment as well
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Create a `.env` file in the root folder and add your Gemini API key:

    ```env
    GOOGLE_API_KEY=your_actual_google_api_key
    ```

2. Run the app:

    ```bash
    streamlit run app.py
    ```

## Explanation

- The `app.py` file contains the main logic of the application. It:
  - Sets up the environment for Hugging Face Spaces using `os.environ["HOME"] = "/tmp"`.
  - Loads the necessary libraries and configures the Gemini model using the Google API key.
  - Allows the user to upload a **resume PDF** and input a **job description**.
  - Provides two options:
    - **HR-Style Resume Review**: Acts like a 10+ year experienced technical HR and gives strengths, weaknesses, and improvement suggestions.
    - **ATS Match Analysis**: Shows match percentage, missing keywords, and final thoughts based on ATS logic.
  - Displays the response and visual metrics such as match percentage using `st.metric` and `st.progress`.

## Additional Notes

- This project is ideal for job seekers targeting roles in Data Science, Full Stack Development, DevOps, AI, or GenAI.
- The tool reads only the **first page** of the resume; for more comprehensive matching, the logic can be extended.
- Deployment-ready for [Hugging Face Spaces](https://huggingface.co/spaces) using `streamlit` SDK and Hugging Face Secrets for key management.
- You can customize prompt templates or scoring logic to better suit your company’s ATS systems or candidate needs.

---


