import streamlit as st
import google.generativeai as genai
from PIL import Image 
from Ia import *

def main():

    with open("style.css") as f:

        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) # Estilo CSS

    with st.sidebar:

        st.image('imagens/Google_Gemini_logo.svg.png',width=150)

        img= st.file_uploader(label='',accept_multiple_files=True)

    with st.container():

        st.header('DESCRIÇÃO DE IMAGENS COM GEMINI')

    with st.container(border=30):

        for x in img:

            if img is not None:
                
                imagem=Image.open(x)

                st.image(imagem)

                IA(imagem)

main() 



