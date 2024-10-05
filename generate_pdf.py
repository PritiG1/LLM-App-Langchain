#
from fpdf import FPDF
import streamlit as st
import base64
from io import BytesIO
# Function to generate a PDF with the dish name, ingredients and recipe
def generate_pdf(dish_name, recipe):
    pdf = FPDF()
    pdf.add_page()

    # Set title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"Dish Name: {dish_name}", ln=True, align='C')

    # Set recipe title
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Ingredients and Recipe:", ln=True)

    # Add recipe content
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(200, 10, txt=recipe)

    # Save the PDF to a buffer and return it as byte stream
    return pdf.output(dest='S').encode('latin1')

def generate_download_link(data, filename, text):
        """Generates a download link for the PDF without refreshing the page."""
        b64 = base64.b64encode(data).decode()  # Convert bytes to base64
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">{text}</a>'
        return href

def display_pdf_download_button(dish_name, recipe):
    """Generate and provide a PDF download button for the recipe."""
    pdf_data = generate_pdf(dish_name, recipe)
    st.sidebar.markdown(
                """ 



                """
            )
    st.sidebar.markdown(
        generate_download_link(pdf_data, f"{dish_name}_recipe.pdf", "Download Recipe"),
        unsafe_allow_html=True
    )


#### Including Hindi as a language option
# from io import BytesIO
# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
# from reportlab.lib import fonts
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch
#
# Function to generate a PDF with Hindi text using ReportLab
# def generate_pdf_hindi(dish_name, recipe):
#     # Create a buffer to hold the PDF data
#     buffer = BytesIO()

#     # Create a PDF document
#     pdf = SimpleDocTemplate(buffer, pagesize=A4,
#                             rightMargin=72, leftMargin=72,
#                             topMargin=72, bottomMargin=18)
    
#     # Define the path to your font file (NotoSansDevanagari or similar)
#     file_path = '/noto-sans-devanagari/NotoSansDevanagari-Light.ttf'

#     # Register the Devanagari font
#     pdfmetrics.registerFont(TTFont('NotoSansDevanagari', file_path))

#     # Get the sample stylesheet
#     styles = getSampleStyleSheet()

#     # Create a custom style for Devanagari (Hindi)
#     hindi_style = styles['Normal']
#     hindi_style.fontName = 'NotoSansDevanagari'
#     hindi_style.fontSize = 12

#     # Create the content list (title and recipe)
#     story = []

#     # Add title with the Unicode font
#     story.append(Paragraph(f"<b>डिश का नाम: {dish_name}</b>", hindi_style))

#     # Add space between title and recipe title
#     story.append(Paragraph("<br/><b>सामग्री और विधि:</b><br/>", hindi_style))

#     # Add the recipe content with auto-wrap
#     story.append(Paragraph(recipe.replace("\n", "<br/>"), hindi_style))  # Replace newlines for paragraphs

#     # Build the PDF
#     pdf.build(story)

#     # Get the PDF content as bytes
#     pdf_data = buffer.getvalue()
#     buffer.close()

#     return pdf_data




