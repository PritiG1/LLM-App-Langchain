from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables from .env file
load_dotenv()
sendgrid_api = os.getenv('sendgrid_apikey')

SENDGRID_API_KEY = sendgrid_api  # Replace with your actual SendGrid API key

    # Function to send email via SendGrid with better formatting
def send_email(email_to, dish_name, recipe):
    # Assuming recipe is a string with ingredients and steps separated by new lines
    formatted_recipe = recipe.replace('\n', '<br>')  # Replace new lines with HTML <br> tags for line breaks

    # Create the HTML content with improved formatting
    email_content = f"""
    <html>
    <body>
        <h1 style="color: #2E86C1;">{dish_name}</h1>
        <h2>Ingredients:</h2>
        <p>{formatted_recipe}</p>
        <h2>Instructions:</h2>
        <p>Follow the steps carefully to make this dish perfect!</p>
    </body>
    </html>
    """

    message = Mail(
        from_email='pritigupta.ds@gmail.com',  # Replace with your email
        to_emails=email_to,
        subject=f"Recipe for {dish_name}",
        html_content=email_content  # Send the formatted recipe as HTML content
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        return str(e)
    

