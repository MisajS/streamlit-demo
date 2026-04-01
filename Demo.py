import streamlit as st

st.write("Hello, World!")


name = st.text_input(" Type in your Name: ")

st.write(f"Hi {name}, Welcome to your first Streamlit")



is_clicked = st.button("Click Me")

if is_clicked:
	st.write("Yoohoo, I got your first hit in Streamlit")



import pandas as pd
data = pd.read_csv("student_scores.csv")
st.write(data)



st.bar_chart(data)
st.line_chart(data)


more_click = st.button("For More, Click me!")
if more_click:
	st.write("visit https://docs.streamlit.io/develop/api-reference")


