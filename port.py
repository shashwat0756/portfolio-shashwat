import streamlit as st
import pandas
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
**Below you can find some of the Apps I have built using Python. Feel free to connect!**
"""
st.write(content2)

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write("**" + row["description"] + "**")
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")
with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write("**" + row["description"] + "**")
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")
