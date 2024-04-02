import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# reading the data from excel file
df = pd.read_excel("Adidas.xlsx")
st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
image = Image.open('adidas-logo.jpg')
st.sidebar.image(image, width=100)


st.title("Adidas Interactive Sales Dashboard")

box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
st.sidebar.write(f"Last updated by:  \n {box_date}")

col1, col2 = st.columns([2,0.8])
with col2:
  fig = go.Figure(data=[go.Bar(x=df["Retailer"], y=df["TotalSales"], 
                             marker=dict(color=df["TotalSales"], colorscale='Viridis'), 
                             text=df["TotalSales"], 
                             hoverinfo='text+y', 
                             )])
fig.update_layout(title="Total Sales by Retailer (3D)", 
                  scene=dict(xaxis_title="Retailer", 
                             yaxis_title="Total Sales", 
                             zaxis_title="Total Sales {$}"), 
                  height=500, 
                  width=900)
st.plotly_chart(fig, use_container_width=True)

_, view1, dwn1, view2, dwn2 = st.columns([0.15,0.20,0.20,0.20,0.20])
with view1:
    expander = st.expander("Retailer wise Sales")
    data = df[["Retailer","TotalSales"]].groupby(by="Retailer")["TotalSales"].sum()
    expander.write(data)
with dwn1:
    st.download_button("Get Data", data = data.to_csv().encode("utf-8"),
                       file_name="RetailerSales.csv", mime="text/csv")

df["Month_Year"] = df["InvoiceDate"].dt.strftime("%b'%y")
result = df.groupby(by = df["Month_Year"])["TotalSales"].sum().reset_index()

with col1:
    fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=result["Month_Year"], y=result["TotalSales"], 
                          mode='lines', name='Total Sales', marker=dict(color='blue')))
fig1.update_layout(title="Total Sales Over Time", 
                   xaxis_title="Month/Year",
                   yaxis_title="Total Sales {$}",
                   template="gridon", 
                   width=900,
                   hovermode="x unified")
fig1.update_traces(hoverinfo="text+name",
                   hovertemplate="Month/Year: %{x}<br>Total Sales: %{y} {$}<extra></extra>")
fig1.update_layout(xaxis=dict(rangeslider=dict(visible=True)))

with col1:
    st.plotly_chart(fig1, use_container_width=True)

with view2:
    expander = st.expander("Monthly Sales")
    data = result
    expander.write(data)
with dwn2:
    st.download_button("Get Data", data = result.to_csv().encode("utf-8"),
                       file_name="Monthly Sales.csv", mime="text/csv")
    
st.sidebar.divider()

result1 = df.groupby(by="State")[["TotalSales","UnitsSold"]].sum().reset_index()

# add the units sold as a line chart on a secondary y-axis
# Main content
fig3 = go.Figure()

# Add Bar chart
fig3.add_trace(go.Bar(x=result1["State"], y=result1["TotalSales"], name="Total Sales", marker_color='skyblue'))

# Add Line chart
fig3.add_trace(go.Scatter(x=result1["State"], y=result1["UnitsSold"], mode="lines", name="Units Sold",
                          yaxis="y2", line=dict(color='red')))

# Update Layout
fig3.update_layout(title="Total Sales and Units Sold by State",
                   xaxis=dict(title="State", tickangle=45),
                   yaxis=dict(title="Total Sales", showgrid=False, rangemode='tozero'),
                   yaxis2=dict(title="Units Sold", overlaying="y", side="right"),
                   template="plotly",
                   legend=dict(x=1, y=1.1),
                   hovermode='x unified')

# Add Hover info
fig3.update_traces(hoverinfo='text', hovertemplate='State: %{x}<br>Total Sales: %{y}')

_, col6 = st.columns([0.1, 1])
with col6:
    st.plotly_chart(fig3, use_container_width=True)
_, view3, dwn3 = st.columns([0.5,0.45,0.45])
with view3:
    expander = st.expander("View Data for Sales by Units Sold")
    expander.write(result1)
with dwn3:
    st.download_button("Get Data", data = result1.to_csv().encode("utf-8"), 
                       file_name = "Sales_by_UnitsSold.csv", mime="text/csv")
st.sidebar.divider()

_, col7 = st.columns([0.1,1])
treemap = df[["Region", "City", "TotalSales"]].groupby(by=["Region", "City"])["TotalSales"].sum().reset_index()


def format_sales(value):
    if value >= 0:
        return '{:.2f} Lakh'.format(value / 1_000_00)


treemap["TotalSales (Formatted)"] = treemap["TotalSales"].apply(format_sales)

fig4 = px.treemap(treemap, path=["Region", "City"], values="TotalSales",
                  hover_name="City",
                  hover_data={"TotalSales (Formatted)": ":.2f Lakh", "Region": False},
                  color="TotalSales",
                  color_continuous_scale='Viridis',
                  height=700, width=900)
fig4.update_traces(textinfo="label+value", hoverinfo="text+name")



with col7:
    st.subheader(":point_right: Total Sales by Region and City in Treemap")
    st.plotly_chart(fig4,use_container_width=True)

_, view4, dwn4 = st.columns([0.5,0.45,0.45])
with view4:
    result2 = df[["Region","City","TotalSales"]].groupby(by=["Region","City"])["TotalSales"].sum()
    expander = st.expander("View data for Total Sales by Region and City")
    expander.write(result2)
with dwn4:
    st.download_button("Get Data", data = result2.to_csv().encode("utf-8"),
                                        file_name="Sales_by_Region.csv", mime="text.csv")

_,view5, dwn5 = st.columns([0.5,0.45,0.45])
with view5:
    expander = st.expander("View Sales Raw Data")
    expander.write(df)
with dwn5:
    st.download_button("Get Raw Data", data = df.to_csv().encode("utf-8"),
                       file_name = "SalesRawData.csv", mime="text/csv")
