# TravelGuide README

> **Note:** This project is still in development and I am working to enhance it in the future.

This is a simple Streamlit web application that generates a personalized travel guide for any city using OpenAI's GPT-4o model via LangChain.

## Features
- Enter a city, month, language, and budget to get a custom travel guide.
- The guide includes must-visit attractions, local cuisine, useful phrases, and budget tips.
- Powered by OpenAI and LangChain.

## Requirements
- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [langchain-openai](https://python.langchain.com/docs/integrations/llms/openai)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install streamlit langchain langchain-openai python-dotenv
   ```
3. **Create a `.env` file** in the project root with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. **Run the app:**
   ```bash
   streamlit run travel_guide.py
   ```

## Usage
- Fill in the city, month, language, and select your budget.
- The app will display a travel guide tailored to your input.

## Example
![screenshot](screenshot.png)

## License
MIT
