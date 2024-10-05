# session_manager.py
import streamlit as st

def initialize_session_state():
    """Initialize session state variables."""
    session_defaults = {
        "button_disabled": False,
        "dropdown_disabled": False,
        "show_email_input": False,
        "dish_name": None,
        "recipe": None,
        "show_share_button": False,
        "show_try_next_button": False
    }

    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def reset_session_state():
    """Reset session state to default."""
    st.session_state["button_disabled"] = False
    st.session_state["dropdown_disabled"] = False
    st.session_state["show_email_input"] = False
    st.session_state["dish_name"] = None
    st.session_state["recipe"] = None
    st.session_state["show_share_button"] = False
    st.session_state["show_try_next_button"] = False
    
