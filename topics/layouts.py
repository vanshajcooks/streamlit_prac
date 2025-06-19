# AAJ hum nazar maarenge layouts pe


import streamlit as st



st.title("Sandwich poll")

col1, col2 = st.columns(2)


with col1:
    st.header("Paneer Sandwich")
    st.image("https://images.pexels.com/photos/32505093/pexels-photo-32505093.jpeg",width=200)
    vote1 = st.button("Vote Paneer sandiwhc")

with col2:
    st.header("club Sandwich")
    st.image("https://images.pexels.com/photos/32560592/pexels-photo-32560592.jpeg",width=200)
    vote2 = st.button("Vote club sandiwhc")


if vote1:
    st.success("Thanks for voting PS")
elif vote2:
    st.success("thanks for CS")


name = st.sidebar.text_input("Enter your name")
sw = st.sidebar.selectbox("Choose your s/w",["CLub","Paneer"])


st.write(f"Welcome {name} and your {sw} s/w is ready!!!")


with st.expander("Show S/w Making instruction"):
    st.write(""""
             1. Prepare slices of bread
             2. Prepare masala required
             3. Put the bread on  pan
             4. spread the mix over 
             4. JOin and READY
             """)
    

st.markdown('### Welcome to my house man')
st.markdown('> blockquote')