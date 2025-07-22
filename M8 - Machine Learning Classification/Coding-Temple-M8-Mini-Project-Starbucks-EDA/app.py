import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and icon
st.set_page_config(page_title="Starbucks Dataset Explorer", page_icon="data/coffee_cup.png")

# Load the dataset
df = pd.read_csv("data/cleaned_starbucks.csv")

# Sidebar navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis"])

# Home Page
if page == "Home":
    st.title("📊 Starbucks Dataset Explorer")
    st.subheader("Welcome to the Starbucks dataset explorer app!")
    st.write("""
        This app provides an interactive platform to explore a Starbucks dataset.
        You can visualize the distribution of data, explore relationships between features, and even make predictions on new data!
        Use the sidebar to navigate through the sections.
    """)
    st.image('https://logos-world.net/wp-content/uploads/2020/09/Starbucks-Logo.png')
    
    
# Data Overview
elif page == "Data Overview":
    st.title("🔢 Data Overview")

    st.subheader("About the Data")
    st.write("""
    This Starbucks dataset contains the **Beverage_prep, Calories, Total Fat (g), Trans Fat (g), Saturated Fat (g), Sodium (mg), 
    Total Carbohydrates (g), Cholesterol (mg)** for each of Starbucks' menu items.
    
    The **Beverage_category** column classifies the type of beverage, such as coffee, tea, or smoothie. 
    ve
    The **Beverage** column provides the specific name of the drink, for instance, Caramel Macchiato or Green Tea Latte.
    
    The **Beverage_prep** column details the preparation method of the beverage, including whether it's served hot or cold, and 
    any additional ingredients or toppings like whipped cream or syrup. The **Calories** column lists the total caloric content 
    of each beverage, providing insight into the energy provided by each drink.
    
    The next three columns, **Total Fat (g)**, **Trans Fat (g)**, and **Saturated Fat (g)**, provide a breakdown of the fat content 
    in each beverage. These columns are crucial for those monitoring their fat intake for health or dietary reasons. The **Sodium (mg)** 
    column indicates the amount of sodium in each beverage, which is essential information for individuals on low-sodium diets.

    The **Total Carbohydrates (g)** column provides the total carbohydrate content, including sugars, which is particularly useful 
    for people managing diabetes or following a low-carb diet. Lastly, the **Cholesterol (mg)** column lists the amount of cholesterol 
    in each beverage, a critical factor for those monitoring their cholesterol levels.

    This dataset serves as a comprehensive guide to the nutritional content of Starbucks beverages, 
    making it a valuable resource for researchers, dietitians, and health-conscious consumers.
    """)
    
    st.image('https://image-cdn.hypb.st/https://hypebeast.com/image/2016/02/starbucks-italy-first-store-00.jpg?w=960&cbr=1&q=90&fit=max')

    # Dataset Display

    st.subheader("Quick Glance at the Data")
    if st.checkbox("Show DataFrame"):
        st.dataframe(df)

    # Shape of Dataset
    if st.checkbox("Show Shape of Data"):
        st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Exploratoxry Data Analysis (EDA)
elif page == "Exploratory Data Analysis":
    st.title("📊 Exploratory Data Analysis (EDA)")

    st.subheader("Select the type of visualization you'd like to explore:")
    eda_type = st.multiselect("Visualization Options", ['Histograms', 'Box Plots', 'Scatterplots', 'Count Plots'])
    
    obj_cols = df.select_dtypes(include='object').columns.tolist()
    num_cols = df.select_dtypes(include='number').columns.tolist()
    
    if 'Histograms' in eda_type:
        st.subheader("Histograms - Visualizing Numerical Distributions")
        h_selected_col = st.selectbox("Select a numerical column for the histogram:", num_cols)
        if h_selected_col:
            chart_title = f"Distribution of {h_selected_col.title().replace('_', ' ')}"
            if st.checkbox("Show by Beverage"):
                st.plotly_chart(px.histogram(df, x=h_selected_col, color='Beverage', title=chart_title, barmode='overlay'))
            else:
                st.plotly_chart(px.histogram(df, x=h_selected_col, title=chart_title))
                
    if 'Box Plots' in eda_type:
        st.subheader("Box Plots - Visualizing Numerical Distributions")
        b_selected_col = st.selectbox("Select a numerical column for the box plot:", num_cols)
        b_selected_col_x = st.selectbox("Select a categorical column for the box plot:", obj_cols)
        if b_selected_col and b_selected_col_x:
            chart_title = f"Distribution of {b_selected_col.title().replace('_', ' ')} by {b_selected_col_x.title().replace('_', ' ')}"
            st.plotly_chart(px.box(df, x=b_selected_col_x, y=b_selected_col, title=chart_title, color=b_selected_col_x))
            # chart_title = f"Distribution of {b_selected_col.title().replace('_', ' ')}"
            # st.plotly_chart(px.box(df, x='species', y=b_selected_col, title=chart_title, color='species'))
            
    if 'Scatterplots' in eda_type:
        st.subheader("Scatterplots - Visualizing Relationships")
        selected_col_x = st.selectbox("Select x-axis variable:", num_cols)
        selected_col_y = st.selectbox("Select y-axis variable:", num_cols)
        if selected_col_x and selected_col_y:
            chart_title = f"{selected_col_x.title().replace('_', ' ')} vs. {selected_col_y.title().replace('_', ' ')}"
            st.plotly_chart(px.scatter(df, x=selected_col_x, y=selected_col_y, title=chart_title))

    if 'Count Plots' in eda_type:
        st.subheader("Count Plots - Visualizing Categorical Distributions")
        selected_col = st.selectbox("Select a categorical variable:", obj_cols)
        if selected_col:
            chart_title = f'Distribution of {selected_col.title()}'
            st.plotly_chart(px.histogram(df, x=selected_col, title=chart_title))
            
