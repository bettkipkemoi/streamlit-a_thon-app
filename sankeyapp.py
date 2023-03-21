# importing libraries
import pandas as pd
import numpy as np
import holoviews as hv
import plotly
import streamlit as st

# add title
st.title('Sankey Diagram - Alluvial Plots in R')

# loading dataset
migration = pd.read_csv('Dataset/migration_nz.csv')