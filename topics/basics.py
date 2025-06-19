import streamlit as st

st.title("Hello world")
st.subheader("Brweed with streamlit")
st.text("welcome ji")
st.write("choose your fav genre")

genre = st.selectbox("Your fav genre: ", ["horror","comedy","scifi"])
st.write(f"great! you like {genre}")

st.success("Your movie has been selected thanks")