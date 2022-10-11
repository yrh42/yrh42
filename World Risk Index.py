import streamlit as st
import pandas as pd
import numpy as np
import plotly as pt
import plotly.express as px
import altair as alt

df=pd.read_csv('C:/Users/lenovo/Downloads/world_risk_index.csv')
st.title("World Risk Analysis")
#st.write(df)

#Visualizing top 5 countries with highest WRI
#st.subheader("Top 5 countries with the highest risk in 2021")
#bar = px.bar(df.head(), x="Region", y="WRI", color="Region")
#st.plotly_chart(bar)

#Visualizing top 5 countries with highest WRI
st.subheader("Top 5 countries with the highest risk in 2021")
st.radio('Pick Region', ['Vanuatu', 'Tonga', 'Salomonen', 'Philippinen', 'Guatemala'])
st.bar_chart(df.head().sort_values('WRI'), x='Region', y='WRI', width=0, height=0, use_container_width=True)
st.write("The tropical island state of Vanuatu has the highest disaster risk, followed by the Solomon Islands and Tonga.")

#Visualizing the effect of Vulnerability and Exposure on the WRI
st.subheader("Effect of Vulnerability and Exposure on the WRI")
scatter_chart = st.altair_chart(
    alt.Chart(df)
        .mark_circle(size=60)
        .encode(x='Exposure', y='Vulnerability', color='WRI')
        .interactive()
)
st.slider('Exposure', 0, 100)
st.write("Risk is at its highest where a high level of exposure to natural hazards coincides with very vulnerable societies.")


#Visualizing impact of Exposure on WRI
st.subheader("Impact of Exposure on World Risk across the years")
fig= px.scatter(df.sort_values('Year'), x="Exposure", y="WRI", color="Region", hover_name="Region", animation_frame="Year", animation_group="Region", log_x=True)
st.plotly_chart(fig)
st.write('Risk is at its highest where a high level of exposure to natural hazards coincides with very vulnerable societies.')

#Visualizing all factors
st.subheader("Relationship of all factors")
fig2 = px.scatter_matrix(df, dimensions=["WRI","Vulnerability", "Exposure", "Susceptibility"], color="Region")
st.plotly_chart(fig2)
st.write("The higher Vulnerability and Exposure, the higher the risk on the countries")


st.balloons()
