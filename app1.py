import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Mesothelioma Analysis")
st.header('Mesothelioma Results from 1988 - 2021')
excel_file = "mesothelioma_data/Mesothelioma.xlsx"
sheet_name = "DATA"
image = Image.open('mesothelioma_data/mesothelioma.webp')
st.image(image, caption='Abestos: The leading cause of mesothelioma cancer cases', use_column_width =True)


df = pd.read_excel(excel_file, sheet_name = 0, usecols="A:D", na_values = "All Cases")
df_diseases = pd.read_excel(excel_file, sheet_name = 0, usecols="A", na_values = "All Cases")
df_diseases.dropna(inplace = True)
df.dropna(inplace = True)
pie_total = px.pie(df,
                    title='Cases of male and female',
                    values='Both',
                    names='Disease Name')
pie_male = px.pie(df,
                    title='Cases of male',
                    values='Male',
                    names='Disease Name')
pie_female = px.pie(df,
                    title='Cases of female',
                    values='Female',
                    names='Disease Name')
                    

st.dataframe(df)
st.dataframe(df_diseases)
st.plotly_chart(pie_total)
st.plotly_chart(pie_male)
st.plotly_chart(pie_female)




