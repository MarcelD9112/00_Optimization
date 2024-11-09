import streamlit as st
import pandas as pd
import plotly.express as px

# Title and File Upload
st.title("Dynamic Data Visualization Dashboard")
st.write("Upload an Excel file to dynamically visualize your data.")

# Upload Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])
if uploaded_file:
    try:
        # Load the data
        df = pd.read_excel(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df)

        # Visualization options
        st.write("### Visualization Options")
        chart_type = st.selectbox("Select Chart Type", ["Bar", "Line", "Scatter", "Pie"])
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns if chart_type != "Pie" else ["None"])

        # Generate chart based on user selection
        st.write("### Generated Chart")
        if chart_type == "Bar":
            fig = px.bar(df, x=x_axis, y=y_axis, title="Bar Chart")
        elif chart_type == "Line":
            fig = px.line(df, x=x_axis, y=y_axis, title="Line Chart")
        elif chart_type == "Scatter":
            fig = px.scatter(df, x=x_axis, y=y_axis, title="Scatter Plot")
        elif chart_type == "Pie":
            fig = px.pie(df, names=x_axis, title="Pie Chart")

        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Error loading file: {e}")

else:
    st.write("Upload an Excel file to get started.")
