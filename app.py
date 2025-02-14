import pandas as pd
import streamlit as st
import plotly.express as px

# reading dataset and changing year column to whole number
df = pd.read_csv('c:/users/user/sdt_project/vehicles_us.csv')
df['model_year'] = df['model_year'].fillna(0).astype(int)

# adding titles
st.header("Car sales listing in US", divider='gray')
st.subheader("_Data viewer_")

# adding data viewer
df1 = df
df1['model_year'] = df1['model_year'].astype(str)
st.write(df1)

# adding scatter plot
st.subheader("_Avg Price vs Model Year by Fuel Type_")
df['model_year'] = df['model_year'].astype(int)
df2 = df[df['model_year'] != 0].groupby(['model_year', 'fuel'])['price'].mean().reset_index(name='average_price')
fig = px.scatter(df2, x='model_year', y='average_price', color='fuel',
                  title='Avg Price vs Model Year by Fuel Type')
fig.update_layout(xaxis_title='Model Year', yaxis_title='Avg Price ($)')
st.plotly_chart(fig)

# adding histogram 1
st.subheader("_Distribution of Vehicle Prices_")
collector = st.checkbox('Show only vintage cars (manufactured before 1980)')
if collector:
    fig1 = px.histogram(df[df['model_year'] < 1980], x='price', nbins=50, title="Distribution of Vehicle Prices")
    fig1.update_layout(xaxis_title='Price ($)', yaxis_title='Count')
    st.plotly_chart(fig1)
else:
    fig1 = px.histogram(df, x='price', nbins=50, title="Distribution of Vehicle Prices")
    fig1.update_layout(xaxis_title='Price ($)', yaxis_title='Count')
    st.plotly_chart(fig1)

# adding histogram 2
st.subheader("_Distribution of Vehicle Odometer Readings_")
fig2 = px.histogram(df, x='odometer', nbins=50, title="Distribution of Vehicle Odometer Readings")
fig2.update_layout(xaxis_title='Odometer (miles)', yaxis_title='Count')
st.plotly_chart(fig2)