## main.py

import streamlit as st
from session_manager import initialize_session_state, reset_session_state
from ui_elements import set_sidebar_style, get_sidebar_inputs
from recipe_generator import generate_dish, display_dish_image
from generate_pdf import display_pdf_download_button
from send_email import send_email
from agent_manager import initialize_price_finder_agent,fetch_ingredient_prices
from extract_ingredients import extract_ingredients

# Initialize session state
initialize_session_state()

# Set sidebar style
set_sidebar_style()

# Get user inputs from the sidebar
cuisine, diet, meal, language = get_sidebar_inputs()

# Go button to trigger generation
go_button = st.sidebar.button("Go", disabled=st.session_state["button_disabled"])

if go_button:
    st.session_state["button_disabled"] = True
    st.session_state["dropdown_disabled"] = True
    st.rerun()

# After rerun, the UI components will be disabled and the fetching begins
if st.session_state["button_disabled"]:
    # Display loading GIF and text
    loading_placeholder = st.empty()
    with loading_placeholder.container():
        st.markdown(
            """
            <div style="display: flex; justify-content: center; padding-bottom: 20px;">
                <img src="https://media.giphy.com/media/d3JtyN73AnQ1E37O/giphy.gif" 
                style="border-radius: 50%; width: 100px; height: 100px;">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div style="text-align: center; font-size: 20px; color: #D3D3D3; font-family: 'Verdana';">
                Please wait while we fetch dish name, ingredients, recipe, and nutritional information...
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Generate dish and recipe
    dish_name, recipe = generate_dish(cuisine, diet, meal, language)
    # Store dish name and recipe in session state
    st.session_state["dish_name"] = dish_name
    st.session_state["recipe"] = recipe

    # Clear the loading message
    loading_placeholder.empty()
    
    # Display dish image
    display_dish_image(dish_name)
    
    # Display dish name and recipe
    st.subheader(f"Dish Name: {dish_name}")
    st.subheader("Ingredients and Recipe")
    st.write(recipe)
    
    # Extract ingredients and display price links using the agent
    ingredients = extract_ingredients(recipe)
    agent_tool = initialize_price_finder_agent()
    fetch_ingredient_prices(agent_tool, ingredients)

    # Provide a PDF download option
    display_pdf_download_button(dish_name, recipe)

    # Re-enable the "Go" button and dropdowns once processing is complete
    st.session_state["button_disabled"] = False
    st.session_state["dropdown_disabled"] = False

    # Set flag to show the Share button after the recipe is fetched
    st.session_state["show_share_button"] = True
    st.session_state["show_try_next_button"] = True  # Show 'Try Next' button after the share button

# --- Add 'Share Recipe' feature ---
if st.session_state.get("show_share_button", False):
    # Add a "Share Recipe" button below the download button
    if st.sidebar.button("Share Recipe"):
        st.session_state["show_email_input"] = True  # Set session state to display the email input

# Display email input and send button if 'Share Recipe' was clicked
if st.session_state["show_email_input"]:
    email = st.sidebar.text_input("Enter email address:")

    if st.sidebar.button("Send"):
        # Ensure that dish_name and recipe are available
        if st.session_state["dish_name"] and st.session_state["recipe"]:
            # Call the function to send email using SendGrid
            status = send_email(email, st.session_state["dish_name"], st.session_state["recipe"])
            if status == 202:
                st.sidebar.write(f"Recipe sent to {email}!")
            else:
                st.sidebar.write(f"Failed to send recipe: {status}")
        else:
            st.sidebar.write("No recipe to share. Please fetch a recipe first.")
        
        # Hide the email input after sending
        st.session_state["show_email_input"] = False

# --- Add 'Try Next' button ---
if st.session_state.get("show_try_next_button", False):
    if st.sidebar.button("Try Next"):
        # Selectively reset session state variables
        reset_session_state()
        # Rerun the app to reflect changes
        st.rerun()
