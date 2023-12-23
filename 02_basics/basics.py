import streamlit as st

st.title("this is my first title")

st.success("This is my first success message")

st.info("This is my first info message")

st.warning("This is my first warning message")

st.error("This is my first error message")

if st.checkbox("show/hide"):
    st.text("showing the widget")


status = st.radio("Select Gender:",("Male", "Female"))

if (status == "Male"):
    st.success("Male")
else:
    st.success("Female")

    
