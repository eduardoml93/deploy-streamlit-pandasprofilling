import pandas as pd
import ydata_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import io
from io import StringIO
import os


def app(title=None):
    st.set_page_config(layout="wide")
    st.title(title)

    # Add a file uploader for CSV files
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Add a select box for choosing the separator
    sep = st.selectbox("Select the separator", ("Comma", "Tab", ";", ":"))
    sep = "," if sep == "Comma" else "\t" if sep == "Tab" else ";" if sep == ";" else ":"

    if uploaded_file is not None:
        # Read the CSV data from the uploaded file
        df = pd.read_csv(StringIO(uploaded_file.getvalue().decode('utf-8')), sep=sep)
        pr = df.profile_report()

        st.title("Dataframe:")
        st.write(df)
        st.title("Pandas Profiling:")
        st_profile_report(pr)

app(title='Pandas Profiling in Streamlit')
