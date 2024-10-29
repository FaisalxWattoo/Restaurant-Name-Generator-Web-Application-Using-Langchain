import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")


# Assuming 'cuisines' is a list of available cuisines
cuisines = ["Indian", "Italian", "Chinese", "Mexican"]

# Create a dropdown menu for selecting cuisine
cuisine = st.sidebar.selectbox("Pick a Cuisine", cuisines)

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(", ")
    st.write("Menu Items")
    for item in menu_items:
        st.write("-", item)


