import streamlit as st
import google.generativeai as genai
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key for the Gemini Pro model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

def scrape_website(url):
    try:
        # Fetch the website content
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract text from the HTML
            text = soup.get_text()
            return text
        else:
            return f"Failed to fetch website. Status code: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

# Prompt template
input_prompt = """
Hey act like a very skilled or experienced web crawller with a deep understanding
 of web pages. Your task is to analyze the content of the provided website and provide a detailed summary.
URL: {url}
"""

# Streamlit app
def main():
    st.title("Website Analyzer with Gemini Pro")

    # Input for website URL
    website_url = st.text_input("Enter the website URL:", "")

    if st.button("Analyze Website"):
        if website_url:
            st.write("Analyzing website...")
            website_text = scrape_website(website_url)
            if website_text:
                st.write("Website content:")
                st.text(website_text)
                input_text = input_prompt.format(url=website_url)
                gemini_response = get_gemini_response(input_text)

                # Write response to markdown file
                with open("gemini_output.md", "w") as f:
                    f.write(gemini_response)

                st.write("Gemini Pro Response:")
                st.markdown(gemini_response, unsafe_allow_html=True)
                st.write("Output written to gemini_output.md")
            else:
                st.write("Failed to analyze website.")
        else:
            st.write("Please enter a website URL.")

if __name__ == "__main__":
    main()
