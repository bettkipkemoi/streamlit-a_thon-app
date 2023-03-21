# importing libraries
import pandas as pd
import numpy as np
import streamlit as st


# add title
st.title('Sankey Diagram (Alluvial Plots in R)')

# loading dataset
migration = pd.read_csv('migration_nz.csv')

st.subheader('Exploring the dataset')
st.dataframe(migration)
st.caption('Dataset Details')
st.text_area('New Zealand Population Migration dataset has information about the number of people who departed from and arrived in New Zealand from all continents and countries of the world from 1979 to 2016.')

# Generating Sankey Diagram
st.plotly_chart(figure_or_data= migration)