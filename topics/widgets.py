import streamlit as st

st.title("Sandwich Maker App")

if st.button("Make a tasty sandwich"):
    st.success("Your sandwich is being made.")

add_cheese = st.checkbox("Add cheese")
if add_cheese:
    st.write("Added cheese to your sandwich")

bread_type = st.radio("Pick your bread: ", ["Brown","White"])

st.write(f"Selected bread is {bread_type}")


spice = st.selectbox("Chooose your spice: ",["Oregano","Chilli flakes"])

st.write(f"Selected spice {spice}")

salt_level = st.slider("Salt level ",0,10,4) # in format min , max ,default

slices = st.number_input("How many slices ", min_value = 1, max_value = 10, step = 1)

st.write(f"Selected slices {slices}")

name = st.text_input("Enter name")
if name:
    st.write(f"Welcome {name}")

dob= st.date_input("Select your date birth")
st.write(f"Born {dob}")