import streamlit as st
from PIL import Image
import datetime

def about():
    st.title("About")
    st.sidebar.image(Image.open('adidas-logo.jpg'), width=100)
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.sidebar.write(f"Last updated by:  \n {box_date}")

    st.write("""
    ## About This App
    This is an interactive sales dashboard for Adidas data.
    
    ## Features
    - Visualize total sales by retailer.
    - View monthly sales trends.
    - Analyze sales by state.
    - Explore total sales by region and city using a treemap.
    
    ## Data Source
    The data used in this dashboard is sourced from an Excel file named `Adidas.xlsx`.
    
    ## Contact
    For any inquiries or feedback, please contact:
    - Email: rnayan2000@gmail.com
    """)

if __name__ == "__main__":
    about()
