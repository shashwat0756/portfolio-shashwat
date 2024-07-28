import streamlit as st
import pandas as pd
my_results = ({"Qualification":["10th","12th","Btech"],"Year":[2018,2020,2024],"Percentage":[76,76,80]})
df1 = pd.DataFrame(my_results)
print(df1)
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/img.jpg",width=502)


with col2:
    st.title("Shashwat Shandilya")
    content= """
    Hi I am Shashwat Shandilya a Python Programmer and I am from Ranchi currently doing Btech in CSE from ITER Bhubhaneswar. I have a deep interest in Data Science and i am currently doing projects in it using different Library functions. I wish to use my
    Technical Skills to contribute to a Team that works at Skill and creates a positive impact on the Society.
    """
    st.info(content)



content2 = """
**Below you can find some of the Apps I have built using Python.
Feel free to connect!**
"""
st.write(content2)

st.sidebar.subheader("Feedback")

st.sidebar.write("Share your opinion")
st.sidebar.write("https://forms.gle/vuUR9sgXjffCocH86")
st.sidebar.subheader("Wish to connect?")
st.sidebar.write("shashwatsandilya514@gmail.com")

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
df = pd.read_csv("data.csv",sep=";")
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
st.table(df1)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)