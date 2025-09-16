import streamlit as st
from pdfextractor import text_extractor
import google.generativeai as genai
import os

#configure the model
key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)
model=genai.GenerativeModel('gemini-2.5-flash-lite')

resume_text=job_desc=None

#upload resume

st.sidebar.title(':blue[UPLOAD YOUR RESUME(pdf only)]')
file=st.sidebar.file_uploader('Resume',type=['pdf'])
if file:
    resume_text=text_extractor(file)

#lets define the main page
st.title(':red[SKILLMATCH]: AI Assistant Skill Matching Tool')
st.markdown('##### this application will match your resume and the job descrption.it will create a detailed report on the match.')       
tips='''Follow these steps to proceed:
* Upload your resume in sidebar(pdf only)
* copy and paste the job descrption below for which you are applying
* click the button and see the magic.'''
st.write(tips)

job_desc=st.text_area('Copy and Paste job description here(press ctrl+enter to run)',max_chars=10000)

prompt=f'''Assume you are an  expert in skill matching. and creating profiles.
Match the following resume with the jobdescrption provided by the user
resume={resume_text}
job_description={job_desc}



your output should as follows
* Give a brief description of the applicant in 3 to 5 lines.
* Give a range expected ATS score along with the matching and non matching keywords
* Give the chances  of getting shotlisted for this position in percentage
* Perform SWOT analysis and discuss each everything in bullet points.
* Suggest what all imporvements can be made in resume in order get better ATS and increase percentage of getting shortlisted.
* Also create two customised resumes as per the descrption provides to get better ATS and increase percentage of getting shortlisted.
* one page resume in such  a format that can be copied and pasted to word and converted into PDF
* use bullet points and tables where ever required.'''



if job_desc:
    if resume_text and job_desc:
        response=model.generate_content(prompt)
        st.write(response.text)
    else:
        st.write('please upload resume')
 