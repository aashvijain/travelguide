from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import PromptTemplate



load_dotenv()  # Loads variables from .env into environment
openai_api_key = os.getenv("OPENAI_API_KEY")
print(f"OpenAI API Key: {openai_api_key}")

llm = ChatOpenAI(model="gpt-4o", api_key=openai_api_key)

prompt_template = PromptTemplate(
    input_variables=["city", "month", "language", "budget"],
    template= """Welcome to the {city} travel guide!
If you're visiting in {month}, here's what you can do:
1. Must-visit attractions.
2. Local cuisine you must try.
3. Useful phrases in {language}.
4. Tips for traveling on a {budget} budget.
Enjoy your trip!"""
)  

st.title("Travel Guide")

city = st.text_input("What is the city: ")
month = st.text_input("What is the month: ")
language = st.text_input("What is the language: ")
budget = st.selectbox ("What is your budget: ", ["low", "medium", "high"])

if city and month and language and budget:
    response = llm.invoke(prompt_template.format(city=city, month=month, language=language, budget=budget))
    st.write(response.content)