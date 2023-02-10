import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

def plot_data(data, plot_type):
    if plot_type == 'line':
        data.plot(kind='line')
    elif plot_type == 'bar':
        data.plot(kind='bar')
    elif plot_type == 'scatter':
        if 'col1' in data.columns and 'col2' in data.columns:
            data.plot(kind='scatter', x='col1', y='col2')
        else:
            st.write("Columns 'col1' and 'col2' not found in data.")
    elif plot_type == 'hist':
        data.plot(kind='hist')
    else:
        st.write("Invalid plot type.")

st.title("Data Visualization Tool")
file_name = st.file_uploader("Upload a CSV file", type="csv")
if file_name is not None:
    data = pd.read_csv(file_name)
    plot_type = st.selectbox("Select the type of plot", ['line', 'bar', 'scatter', 'hist'])
    plot_data(data, plot_type)
    matplotlib.use("Agg")
    st.pyplot()
