from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI




load_dotenv()

API_KEY = os.environ['OPENAI_API_KEY']
llm = OpenAI(API_KEY)

pandas_ai = PandasAI(llm)

st.title('Prompt-Driven Analysis Tool')
uploded_file = st.file_uploader('Uplode Your CSV File Here🗂️',type=['csv'])

if uploded_file is not None:
    df = pd.read_csv(uploded_file)
    st.write(df.head())
    
    prompt = st.text_area('Enter Your prompt 💬')

    if st.button('Generate'):
        if prompt:
           with st.spinner('Generating'):
                st.write(pandas_ai.run(df , prompt=prompt))

        else:
            st.warning('Please Enter A Prompt ⦰')

