# webrequest karege
import streamlit as st
import requests
st.title("Live currency convertor")
amount = st.number_input("Enter the amount in INR", min_value= 1)


target_currency=st.selectbox("Convert to:", ["USD","EUR","GBP","JPY"])

if st.button("Convert"):
    url = "https://v6.exchangerate-api.com/v6/69aee23b58d0ffa604a81b7d/latest/INR"
    response = requests.get(url)

    if response.status_code==200:
        data = response.json()
        rate = data["conversion_rates"][target_currency]
        converted = rate*amount
        st.success(f"{amount} INR = {converted} {target_currency}")
    else:
        st.error("failed to fetch")
