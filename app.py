import streamlit as st
import pandas as pd
from CSV_Data_Analytics.helper import *




# Streamlit app configuration
st.set_page_config(layout='wide')
st.title("CSV Data Analytics Platform")

# Multi-file uploader
uploaded_files = st.file_uploader(
    "Upload your CSV file(s)", type=['csv'], accept_multiple_files=True
)

if uploaded_files:
    combined_data = pd.DataFrame()

    # Display uploaded files and combine them
    st.subheader("Uploaded Files")
    for file in uploaded_files:
        st.write(f"✅ {file.name}")
        data = pd.read_csv(file)
        combined_data = pd.concat([combined_data, data], ignore_index=True)

    st.success("Files Uploaded Successfully")

    # Display dataset summary
    st.header("Dataset Summary")
    st.markdown(generate_summary(combined_data))

    # Data preview
    st.header("Data Preview")
    st.dataframe(combined_data, use_container_width=True)

    # Interactive query-based analytics
    st.header("Actionable Insights")
    query = st.text_area("Enter your query about the data", placeholder="E.g., What is the average sales?")
    if st.button("Analyze Data"):
        if query.strip():
            result = chat_with_csv(combined_data, query)
            st.subheader("Query Result")
            st.success(result)
        else:
            st.warning("Please enter a valid query.")

    # Detailed reports section
    st.header("Detailed Reports")
    if st.button("Generate Report"):
        st.download_button(
            label="Download Report",
            data=combined_data.to_csv(index=False),
            file_name="detailed_report.csv",
            mime="text/csv"
        )
        st.success("Detailed report is ready for download.")

    # Visualizations
    visualize_data(combined_data)
else:
    st.info("Please upload at least one CSV file to get started.")
