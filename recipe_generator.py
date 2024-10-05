# recipe_generator.py
import time
import streamlit as st
from langchain_helper import sequential_chain
from fetch_image import fetch_image_from_google


def generate_dish(cuisine, diet, meal, language):
    """Generate dish name and recipe based on user input."""
    time.sleep(2)  # Simulate fetch process
    dish_name, recipe = sequential_chain(cuisine, diet, meal, language, "llama3.1")
    return dish_name, recipe

def display_dish_image(dish_name):
    """Fetch and display the dish image."""
    image_url = fetch_image_from_google(dish_name)
    if image_url:
        st.sidebar.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="{image_url}" style="border-radius: 50%; width: 150px; height: 150px;">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.sidebar.write("Image not found for the dish.")
