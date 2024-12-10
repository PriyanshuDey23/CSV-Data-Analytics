import streamlit as st
import os
from pandasai import Agent
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import seaborn as sns


# Load environment variables
load_dotenv()
pandasai_api_key = os.getenv("PANDASAI_API_KEY")
os.environ["PANDASAI_API_KEY"] = pandasai_api_key

# Helper function for conversational data analysis
def chat_with_csv(df, prompt):
    agent = Agent(df)
    result = agent.chat(prompt)
    return result

# Improved summary generation
def generate_summary(df):
    summary = f"""
    **Dataset Summary**
    - **Number of Rows**: {len(df):,}
    - **Number of Columns**: {len(df.columns):,}
    - **Missing Values**: {df.isnull().sum().sum():,}
    - **Duplicate Rows**: {df.duplicated().sum():,}

    **Columns Overview**
    - {', '.join(df.columns)}
    """
    return summary

# Visualization helper function
def visualize_data(df):
    st.subheader("Visual Data Representation")
    numeric_columns = df.select_dtypes(include=["number"]).columns

    if not numeric_columns.any():
        st.warning("No numeric columns available for visualization.")
        return

    st.write("### Select a Chart Type:")
    chart_type = st.radio(
        "Chart Type",
        ("Bar Chart", "Line Chart", "Histogram", "Correlation Heatmap", "Scatter Plot")
    )

    if chart_type == "Bar Chart":
        column = st.selectbox("Select a column for Bar Chart", numeric_columns)
        st.bar_chart(df[column])

    elif chart_type == "Line Chart":
        column = st.selectbox("Select a column for Line Chart", numeric_columns)
        st.line_chart(df[column])

    elif chart_type == "Histogram":
        column = st.selectbox("Select a column for Histogram", numeric_columns)
        bins = st.slider("Number of bins", min_value=5, max_value=50, value=20)
        fig, ax = plt.subplots()
        sns.histplot(df[column], bins=bins, ax=ax, kde=True)
        st.pyplot(fig)

    elif chart_type == "Correlation Heatmap":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df[numeric_columns].corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    elif chart_type == "Scatter Plot":
        col1, col2 = st.columns(2)
        x_col = col1.selectbox("X-axis", numeric_columns)
        y_col = col2.selectbox("Y-axis", numeric_columns)
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
        st.pyplot(fig)