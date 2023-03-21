# importing libraries
import pandas as pd
import numpy as np
import streamlit as st
import plotly.figure_factory as ff


# add title
st.title('Sankey Diagram (Alluvial Plots in R)')

# loading dataset
migration = pd.read_csv('migration_nz.csv')

st.subheader('Exploring the dataset')
st.dataframe(migration)
st.caption('Dataset Details')
st.text_area('New Zealand Population Migration dataset has information about the number of people who departed from and arrived in New Zealand from all continents and countries of the world from 1979 to 2016.')

# Generating Sankey Diagram
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],
      color = "blue"
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2]
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()