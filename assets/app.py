import streamlit as st

st.set_page_config(page_title="Weather App")

st.title("🌤 Weather Forecast App")

city = st.text_input("Enter City")

if st.button("Search"):
    st.success(f"You entered: {city}")