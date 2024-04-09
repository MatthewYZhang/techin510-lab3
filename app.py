import os
from dataclasses import dataclass
import datetime

import streamlit as st
import psycopg2
from dotenv import load_dotenv

load_dotenv()

con = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = con.cursor()

@dataclass
class Prompt:
    id: int = None
    title: str
    prompt: str
    is_favorite: bool = False
    created_at: datetime.datetime

def prompt_form(prompt=Prompt('', '')):
    with st.form(key='prompt_form', clear_on_submit=True):
        title = st.text_input('Title', value=prompt.title)
        prompt_text = st.text_area('Prompt', value=prompt.prompt)
        is_favorite = st.checkbox('Favorite', value=prompt.is_favorite)

        submitted = st.form_submit_button('Submit')
        if submitted:
            return Prompt()
        

st.title('Prompt Storage')
st.subheader('A simple app to sotre and retrieve prompts')

