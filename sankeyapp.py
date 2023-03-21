# importing libraries
import pandas as pd
import numpy as np
import streamlit as st

# add title
st.title('Sankey Diagram - Alluvial Plots in R')

# loading dataset
migration = pd.read_csv('migration_nz.csv')