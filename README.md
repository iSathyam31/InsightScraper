## Introduction
This is a Python application that leverages Google's Gemini Pro model to analyze the content of a website and generate insightful summaries. It utilizes web scraping techniques to extract textual content from a given URL and then processes this content through the Gemini Pro model to provide detailed insights.


## Installation
To set up the environment and install the required dependencies, follow these steps:

1. Clone the repository:
```
git clone https://github.com/iSathyam31/InsightScraper.git
```

2. Navigate to the project directory:

3. Create a virtual environment and activate it(optional but recommended):
```
conda create -p venv python=3.11 -y
conda activate venv/
```

4. Install the required packages:
```
pip install -r requirements.txt
```


## Usage

To run the GeminiWeb Analyzer, follow these steps:

1. Ensure that your virtual environment is activated (if you created one).

2. Run the Streamlit app:
```
streamlit run main.py
```


3. Open your web browser and navigate to the provided URL (typically http://localhost:8501).

4. Enter the URL of the website you want to analyze in the input field.

5. Click on the "Analyze Website" button.

6. Wait for the analysis to complete. The app will display the website content and the generated summary from the Gemini Pro model.


## Dependencies

- [Streamlit](https://streamlit.io/)
- [Google's GenerativeAI](https://pypi.org/project/google-generativeai/)
- [Requests](https://pypi.org/project/requests/)
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)

## Contributing

Contributions to GeminiWeb Analyzer are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.