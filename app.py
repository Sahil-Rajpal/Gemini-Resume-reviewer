import os
os.environ["HOME"] = "/tmp"


from dotenv import load_dotenv


load_dotenv()
import streamlit as st

import io
import base64
from PIL import Image
import pdf2image
import fitz  # PyMuPDF
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text


# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         ## convert the pdf to image
#         images=pdf2image.convert_from_bytes(uploaded_file.read())


#         first_page=images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")
    

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Open the PDF file from the uploaded stream
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        # Take the first page and convert to image
        first_page = pdf_document[0]
        pix = first_page.get_pixmap()

        # Convert to byte array
        img_bytes = pix.tobytes("png")
        img_byte_arr = io.BytesIO(img_bytes)

        # Prepare data for Gemini
        pdf_parts = [
            {
                "mime_type": "image/png",
                "data": base64.b64encode(img_byte_arr.getvalue()).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")



## streamlit app















st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description : ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)... ",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1=st.button("Tell me About the Resume") 

# submit2=st.button("How can I improvise me Skill")

# submit3=st.button("What are the Keywords that are Missing")

submit3=st.button("Percentage Match") 

# You are an experienced Technical Human Resource Manager with Experience of 10 years in the field of any one job role of Data Science , Full Stack Web Development,Big Data Engineering,Devops,Data Analyst ,AI Engineer , Gen AI engineer.
# your task is to review the provided resume against the job description provided for these profiles.
#   Please share your professional evaluation on whether the candidate's profile aligns with the role. 
#  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
#  And Also give (in a different section) how a candidate should make changes in description of existing projects or make a new one so that the missing words can be 
#  included in it and also should not look fishy.



# You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science , Full Stack Web Development,Big Data Engineering,Devops,Data Analyst and deep ATS functionality, 
# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
# the job description. First the output should come as percentage and then keywords missing and last final thoughts.


input_prompt1="""


Act as a Technical Human Resource Manager with 10+ years of experience in hiring for technical roles including Data Science, Full Stack Web Development, Big Data Engineering, DevOps, Data Analyst, AI Engineering, and GenAI Engineering.

Your task is to **evaluate the provided resume** against the job description (JD) for one of these roles.

Please provide your analysis in the following format:

1. **Overall Fit Assessment**:  
   - Does the candidate meet the core job requirements?  
   - What role does the resume most closely align with?

2. **Strengths**:  
   - List relevant skills, tools, experiences, or certifications that are aligned with the JD.

3. **Weaknesses / Gaps**:  
   - Mention areas where the resume lacks alignment with the JD.

4. **Improvement Suggestions**:  
   - Suggest how the candidate can rephrase or enhance existing projects to naturally include missing keywords or relevant technologies.  
   - Optionally, suggest a new project idea that can cover missing aspects without sounding artificial.

Please format your response in **clear markdown with bold section headers**, and keep the tone professional and constructive.
"""


input_prompt3 = """

You are an advanced ATS (Applicant Tracking System) analyzer with deep knowledge of how resumes are parsed and matched against job descriptions in domains like Data Science, Full Stack Development, Big Data Engineering, DevOps,Data Analyst and AI.

Evaluate the provided resume against the given job description using the following structure:

1. **Match Percentage**:  
   - Give a precise match percentage (e.g., 76%) based on skills, technologies, keywords, and role-specific criteria.

2. **Missing or Weak Keywords**:  
   - List specific technical keywords, tools, or phrases missing or weakly represented in the resume that are important for the JD.

3. **Final Thoughts**:  
   - Short summary of what could be done to improve the match score. Be objective, and suggest next steps to enhance alignment.

Please format your response with bullet points and bold section headers for better readability.
"""




if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is ")
        st.write(response)
    else:
        st.write("Please Upload the Resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is ")
        st.write(response)
        import re

        # Extract percentage
        match = re.search(r'(\d+)%', response)
        if match:
            match_percentage = int(match.group(1))
            st.progress(match_percentage)
            st.metric(label="Match Score", value=f"{match_percentage}%")
    else:
        st.write("Please Upload the Resume")
            