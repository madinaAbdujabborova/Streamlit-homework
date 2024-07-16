import streamlit as st
import pandas as pd
import time
import numpy as np

# Booshidagi Introduction uchun

st.write("# Fastfood Nutrition")
st.write("### Which fast food products are worst for you?")
st.write("""##### Welcome to the Fast Food Nutrition Dataset, which provides a comprehensive breakdown of the nutritional content of various fast food products from popular fast food chains. Fast food is known for its convenience and affordability, but it is also infamous for its high-calorie, high-fat, and high-sugar content. This dataset aims to shed light on the nutritional value of these fast food products, helping consumers make more informed decisions about their food choices. With information on calories, fat, carbohydrates, protein, and other key nutrients, this dataset provides a valuable resource for nutritionists, researchers, and health-conscious individuals. By analyzing this dataset, we can gain a better understanding of the nutritional impact of fast food consumption and work towards creating healthier food options in the fast food industry.""")

df = pd.read_csv("fastfood.csv")

# Tabs orqali chart va jadvalni ko'rish

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart restaurants")
tab1.bar_chart(df["restaurant"])

tab2.subheader("A tab with the data calories")
tab2.write(df["calories"])

# Side bar qo'shish chap tomonda

with st.sidebar:
    
    st.line_chart(df.groupby('restaurant')['protein'].mean(), y_label="Protein index", x_label="Restaurants")
    
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

# Button qo'shib jadval ko'rsatish

restaurant = st.radio(
    label = "Please, select any restaurant",
    options = df['restaurant'].unique().tolist(),
    index=None,
)

if st.button("Show the table"):
    # st.write("Why hello there")
    st.write("You selected:", restaurant)
    
    st.dataframe(df[df["restaurant"]==restaurant])
else:
    pass

# Line chart
st.line_chart(df.groupby('restaurant')['trans_fat'].mean(), y_label="Trans fat", x_label="Restaurants")
