import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='whitegrid')

total_orders = pd.read_csv("total_orders.csv")
product_rfm = pd.read_csv("product_rfm.csv")
st.title(":green[E-Commerce] Product Analysis:gift:")
st.caption("Wayan Abin Bena Bimantara")




st.subheader("Product Based on Review Score:star:")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x="number_of_orders", 
            y="label", data=total_orders, 
            estimator="sum", 
            errorbar = None)
    
plt.xlabel(None)
plt.ylabel(None)
plt.title("Total Selling High Score vs Low Score")

st.pyplot(fig)


with st.expander("See Details"):
    col1, col2 = st.columns(2)
    with col1:
        total_product= total_orders["product_id"].nunique()
        st.metric("Total Product:", value=total_product)

    with col2:
        avg= total_orders["number_of_orders"].mean().round()
        avg= int(avg)
        st.metric("Average Selling", value=avg)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
    sns.barplot(x="review_score", 
                y="number_of_orders", 
                hue = "label", 
                data=total_orders,
                estimator="sum", errorbar = None,
                ax=ax[0])
    ax[0].set_title("Total Selling")
    ax[0].set_xlabel(None)
    ax[0].set_ylabel(None)

    sns.barplot(x="review_score", 
                y="number_of_orders", 
                hue = "label", 
                data=total_orders, 
                estimator="mean", errorbar = None,
                ax=ax[1])
    ax[1].set_title("Average Selling")
    ax[1].set_xlabel(None)
    ax[1].set_ylabel(None)

    plt.suptitle("Product Selling Based on Review Score", fontsize=20)
    st.pyplot(fig)
   

st.subheader('Top 5 Product Based on RFM:bar_chart:')

col1, col2 = st.columns(2) 
with col1:
    freq= product_rfm["frequency"].max()
    st.metric("Highest frequency:", value=freq)
 
with col2:
    rev= product_rfm["monetary"].sum().round(1)
    st.metric("Total Revenue", value=rev)

tab1, tab2 , tab3= st.tabs(["Recently", "Frequently", "Monetary"])

with tab1:
    st.subheader("Recency")
    fig, ax = plt.subplots(nrows=3,ncols=1,figsize=(12, 18))

    sns.barplot(y="recency", 
            x="product_id", 
            data=product_rfm.sort_values("recency",ascending=True).head(5),
            ax = ax[0])
    ax[0].set_title("Recency (days)")
    ax[0].set_xlabel(None)
    ax[0].set_ylabel(None)
    ax[0].tick_params(axis="x", labelsize=7)

    sns.barplot(y="frequency", 
                x="product_id", 
                data=product_rfm.sort_values("recency",ascending=True).head(5),
                ax = ax[1])
    ax[1].set_title("Frequency")
    ax[1].set_xlabel(None)
    ax[1].set_ylabel(None)
    ax[1].tick_params(axis="x", labelsize=7)
    
    sns.barplot(y="monetary", 
                x="product_id", 
               data=product_rfm.sort_values("recency",ascending=True).head(5),
               ax = ax[2])
    ax[2].set_title("Monetary")
    ax[2].set_xlabel(None)
    ax[2].set_ylabel(None)
    ax[2].tick_params(axis="x", labelsize=7)

    st.pyplot(fig)
    
with tab2:
    st.subheader("Frequency")
    fig, ax = plt.subplots(nrows=3,ncols=1,figsize=(12, 18))

    sns.barplot(y="recency", 
                x="product_id", 
                data=product_rfm.sort_values("frequency",ascending=False).head(5),
                ax = ax[1])
    ax[1].set_title("Recency (days)")
    ax[1].set_xlabel(None)
    ax[1].set_ylabel(None)
    ax[1].tick_params(axis="x", labelsize=7)

    sns.barplot(y="frequency", 
                x="product_id", 
                data=product_rfm.sort_values("frequency",ascending=False).head(5),
                ax = ax[0])
    ax[0].set_title("Frequency")
    ax[0].set_xlabel(None)
    ax[0].set_ylabel(None)
    ax[0].tick_params(axis="x", labelsize=7)

    sns.barplot(y="monetary", 
                x="product_id", 
                data=product_rfm.sort_values("frequency",ascending=False).head(5),
                ax = ax[2])
    ax[2].set_title("Monetary")
    ax[2].set_xlabel(None)
    ax[2].set_ylabel(None)
    ax[2].tick_params(axis="x", labelsize=7)

    st.pyplot(fig)

with tab3:
    st.subheader("Monetary")
    fig, ax = plt.subplots(nrows=3,ncols=1,figsize=(12, 18))

    sns.barplot(y="recency", 
                x="product_id", 
                data=product_rfm.sort_values("monetary",ascending=False).head(5),
                ax = ax[2])
    ax[2].set_title("Recency (days)")
    ax[2].set_xlabel(None)
    ax[2].set_ylabel(None)
    ax[2].tick_params(axis="x", labelsize=7)

    sns.barplot(y="frequency", 
                x="product_id", 
                data=product_rfm.sort_values("monetary",ascending=False).head(5),
                ax = ax[1])
    ax[1].set_title("Frequency")
    ax[1].set_xlabel(None)
    ax[1].set_ylabel(None)
    ax[1].tick_params(axis="x", labelsize=7)

    sns.barplot(y="monetary", 
                x="product_id", 
                data=product_rfm.sort_values("monetary",ascending=False).head(5),
                ax = ax[0])
    ax[0].set_title("Monetary")
    ax[0].set_xlabel(None)
    ax[0].set_ylabel(None)
    ax[0].tick_params(axis="x", labelsize=7)

    st.pyplot(fig)