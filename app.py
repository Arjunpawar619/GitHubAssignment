import streamlit as st

st.title("Campusx")

c1 , c2 = st.columns(1)

with c1:
    st.write(" abcd efg") 

st.header("Courses")
st.subheader("Data Analytics and ML ")
st.subheader("DSA")

st.subheader('OPP')

st.button("menu_button")

