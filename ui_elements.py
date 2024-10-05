# ui_elements.py

import streamlit as st

def set_sidebar_style():
    """Set custom styling for the sidebar."""
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: #C8F4F7;  /* Light blue */
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

def get_sidebar_inputs():
    """Get user inputs from the sidebar."""
    st.title("What's Cooking Today :stew:?")
    cuisine = st.sidebar.selectbox("Select Cuisine", 
                                   ["Italian", "Indian", "Chinese", "Mexican", "Japanese", "Middle East", "Spanish"], 
                                   disabled=st.session_state["dropdown_disabled"])
    diet = st.sidebar.selectbox("Select Diet Type", 
                                ["Vegetarian", "Vegan", "Meat-Based", "Seafood"], 
                                disabled=st.session_state["dropdown_disabled"])
    meal = st.sidebar.selectbox("Select Meal", 
                                ["Breakfast", "Lunch", "Dinner"], 
                                disabled=st.session_state["dropdown_disabled"])
    language = st.sidebar.selectbox("Select Language", 
                                    ["English", "French", "Spanish"], 
                                    disabled=st.session_state["dropdown_disabled"])
    return cuisine, diet, meal, language
