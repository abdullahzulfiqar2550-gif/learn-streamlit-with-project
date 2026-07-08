import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Sales Analysis Project",
    layout='wide'
)

st.title("Sales Analysis Project")

min_sales = st.sidebar.number_input(
    "Minimum Sales Value",
    min_value=1000,
    value=5000,
    key="min_sales"
)

max_sales = st.sidebar.number_input(
    "Maximum Sales Value",
    min_value=min_sales,
    value=10000,
    key="max_sales"
)

min_profit = st.sidebar.number_input(
    "Minimum Profit Value",
    min_value=1000,
    value=10000,
    key="min_profit"
)

max_profit = st.sidebar.number_input(
    "Maximum Profit Value",
    min_value=min_profit,
    value=20000,
    key="max_profit"
)

generate_data = st.sidebar.button(
    "Generate Dataset",
    key="generate_Sales_data"
)
if generate_data:
    np.random.seed(10)
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    df= pd.DataFrame({
    "Month": month,
    "Sales": np.random.randint(min_sales, max_sales +1, 12),
    "Profit": np.random.randint(min_profit, max_profit +1, 12),
    "Orders" : np.random.randint(100, 500+1, 12),
    "Customers" : np.random.randint(50, 300 +1, 12)
    })

    st.subheader("Generated Dataset")
    st.dataframe(df)

    st.subheader("Basic Calculations")

    st.write("Average Sales")
    st.write(round(df["Sales"].mean(), 2))

    st.write("Average Profit")
    st.write(round(df["Profit"].mean(), 2))

    st.write("Total Sales")
    st.write(round(df["Sales"].sum(), 2))

    st.write("Total Profit")
    st.write(round(df["Profit"].sum(), 2))

    st.write("Summary Statistics")
    st.write(df.describe())

    st.subheader("Sales Histogram")
    fig, ax = plt.subplots()
    ax.hist(
        df["Sales"],
        bins=10
    )
    st.subheader("Sales Distribution")
    st.pyplot(fig)

    st.subheader("Profit Histogram")
    fig, ax = plt.subplots()
    ax.hist(
        df["Profit"],
        bins=10)

    ax.set_title("Profit Distribution")
    st.pyplot(fig)

    st.subheader("Monthly Sales Trend")

    fig, ax = plt.subplots()
    ax.plot(
        df["Month"],
        df["Sales"],
        marker="o")

    ax.set_title("Monthly Sales Trend")
    st.pyplot(fig)


    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(
        df.select_dtypes(include=np.number).corr(),
        annot=True,
        cmap="Blues",
        ax=ax)
    st.pyplot(fig)

    st.subheader("Sales vs Profit Interactive Chart")
    fig = px.line(
        df,
        x="Month",
        y=["Sales", "Profit"],
        markers=True,
        title="Sales and Profit Trend")

    st.plotly_chart(
        fig,
        use_container_width=True )
else:
    st.info("Select inputs from the sidebar and click Generate Dataset")