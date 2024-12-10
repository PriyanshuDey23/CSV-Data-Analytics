
# CSV Data Analytics

## Overview
This application allows users to upload and analyze multiple CSV files interactively. With features like advanced analytics, actionable insights, detailed reports, and visual data representation, it simplifies data exploration and decision-making.

## Features
1. **Enhanced Analytics**: 
   - Upload and merge multiple CSV files.
   - Combine and analyze datasets effortlessly.

2. **Actionable Insights**:
   - Ask questions about your data and get instant responses.

3. **Detailed Reports**:
   - Download comprehensive CSV reports to share with your team.

4. **Visual Data Representation**:
   - Create intuitive visualizations like bar charts, line charts, histograms, scatter plots, and correlation heatmaps.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Interactive user interface.
- **Pandas**: Data manipulation and processing.
- **PandasAI**: Conversational data analytics.
- **Matplotlib & Seaborn**: Advanced data visualization.
- **dotenv**: Secure API key handling.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/PriyanshuDey23/CSV-Data-Analytics.git

   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your **PandasAI** API key:
   - Obtain your API key from [PandasAI](https://www.pandabi.ai/admin/api-keys).
   - Create a `.env` file in the project directory and add your API key:
     ```
     PANDASAI_API_KEY=your_api_key_here
     ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser using the URL provided in the terminal.

3. Upload one or more CSV files using the uploader.

4. Explore the data, ask queries, generate reports, and create visualizations.

## Example Queries
- "What is the average value of column X?"
- "Show the total sales grouped by category."

## Visualizations
- Bar Chart
- Line Chart
- Histogram
- Scatter Plot
- Correlation Heatmap

## Contributions
Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/your-repo/issues).

## License
This project is licensed under the MIT License.


