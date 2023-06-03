import streamlit as st
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/img.jpg")

with col2:
    st.title("Shashwat Shandilya")
    content= """
    Hi I am Shashwat Shandilya a Python Programmer 
    """
    st.info(content)
