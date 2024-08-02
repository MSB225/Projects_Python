import google.generativeai as genai
from PIL import Image 
import streamlit as st
import os

def IA(imagem):

    API_KEY=os.environ['API_KEY']=st.secrets['API_KEY']

    genai.configure(api_key=API_KEY)

    model=genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(imagem)

    return st.write(response.text)


