import streamlit as st
from PIL import Image
import datetime

def finding():
    st.title("Findings")
    st.sidebar.image(Image.open('adidas-logo.jpg'), width=100)
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.sidebar.write(f"Last updated by:  \n {box_date}")

    st.write("""
    ## Total sales  over time
- Shows total sales over time with peaks and valleys
- Clear cyclical/seasonal pattern in the sales data
- Sales peak around September/October and March/April each year
- Sales dip around November/December and May/June each year
- Highest peaks indicate busiest/peak sales seasons
- Lowest points represent slowest/off-peak sales periods
- Recurring up-and-down cycle suggests seasonal fluctuations in demand
- Allows identification of predictable sales trends and patterns
- Useful for business planning and resource allocation aligned with cycles
    
    ## Total sales by Retailer
    Based on the graph showing total sales by retailer, here are the key findings:

1. Foot Locker appears to be the top-performing retailer in terms of total sales, having the tallest bar indicating the highest sales figures.

2. Sports Direct and West Gear are the next two highest performers in sales among the retailers shown.

3. Walmart, while a major retailer, has lower total sales compared to Foot Locker, Sports Direct, and West Gear in this particular data set.

4. Kohl's and Amazon have the lowest total sales figures among the retailers presented in the graph.

5. There is a significant gap between the top performers (Foot Locker, Sports Direct, West Gear) and the bottom performers (Kohl's, Amazon) in terms of total sales.

6. The graph suggests that sporting goods/athletic retailers like Foot Locker, Sports Direct, and West Gear have higher sales compared to general merchandisers like Walmart, Kohl's, and Amazon for the product category or market represented in this data.

    
    ## Total Sales And Units Sold By State
  Based on the graph showing total sales and units sold by state, here are the key findings:

1. The states with the highest total sales appear to be California, Texas, Florida, and New York. These states have the tallest blue bars, indicating the largest sales figures.

2. The states with the highest units sold seem to be California, Texas, Florida, and Illinois. These states have the tallest orange bars, representing the highest unit sales volumes.

3. There appears to be a general correlation between high total sales and high units sold for most states, with some exceptions. States with larger populations and economies tend to have both higher sales revenue and unit sales.

4. However, there are a few states where the total sales and unit sales do not align as closely, such as New York having relatively higher total sales compared to its units sold.

5. The graph shows significant variations in both total sales and units sold across different states, likely reflecting factors such as population size, economic conditions, and market demand in each state.

6. Some states have relatively low total sales and unit sales compared to others, suggesting potential opportunities for growth or expansion in those markets.

    
    ## Contact
    For any inquiries or feedback, please contact:
    - Email: rnayan2000@gmail.com
    """)

if __name__ == "__main__":
    finding()