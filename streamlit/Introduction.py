
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Introduction", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items={
    "About": "https://www.linkedin.com/in/zschmitz https://github.com/Zacharia-Schmitz"
})

# TO RUN THIS:
# IN TERMINAL PUT:
# streamlit run Introduction.py

# DEMO APP:
# streamlit hello

# Load the data
@st.cache_resource
def load_data():
    return pd.read_csv('../support_files/working_docs/top_skills.csv')

top_skills_df = load_data()

@st.cache_resource
def load_full_data():
    return pd.read_csv('../support_files/working_docs/jobs_prepped.csv')

jobs_df_cleaned = load_full_data()

def load_original_data():
    return pd.read_csv('../support_files/working_docs/jobs_stripped.csv')

data = load_original_data()

st.markdown("""
# Introduction

Words and things

# Project Summary

More words and things

### Planning

Words

""")

st.dataframe(data)

st.markdown("""
### Preparation

Words
""")

st.dataframe(jobs_df_cleaned)

st.markdown("""

### Exploration

Words

### Modeling

Words

### Delivery

Words

""")