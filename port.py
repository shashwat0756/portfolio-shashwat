import streamlit as st
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/img.jpg",width=500)


with col2:
    st.title("Shashwat Shandilya")
    content= """
    Hi I am Shashwat Shandilya a Python Programmer 
    """
    st.info(content)

content2 = """
Below you can find some of the Apps I have built using Python. Feel free to connect!
"""
st.write(content2)