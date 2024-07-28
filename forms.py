import streamlit as st
st.title("Feedback")

with st.form(key="forms"):
    Name = st.text_input("Your Name")
    message = st.text_area("Suggestions")
    button = st.form_submit_button("**Submit**")