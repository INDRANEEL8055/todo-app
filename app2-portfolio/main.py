import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Indraneel Jain")
    content = """ Hi , I am a python developer, 
     i graduated in 2020,
     i worked at Infosys with 2 years of experience
     on Python,sql,oracle\n\nWELCOME to my Portfolio   """
    st.info(content)

content2 = """ Below you can find 
               some of the projects that
                i worked upon....."""

st.write(content2)

col3, col4 = st.columns(2)  # dividing the my projects in two coloumns

df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

