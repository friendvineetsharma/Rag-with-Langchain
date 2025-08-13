import google.generativeai as genai
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    try:
        print(demo.__doc__)
        demo()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure your API key is correct and properly configured.")

def demo():
    """A simple demonstration of using Google Generative AI with LangChain."""

    # Initialize the GoogleGenerativeAI with the API key and the new model name
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    
    # Correct way to instantiate the model: pass the model name directly
    # 'gemini-1.5-flash' is a great alternative to 'gemini-1.5-pro'
    model = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.environ.get("GEMINI_API_KEY"))

    # Create a chat prompt template
    prompt = ChatPromptTemplate.from_template("Tell me a few words about {name}")

    # Create a chain with the prompt and model
    chain = prompt | model 

    print(chain.invoke({"name": "Maharana Pratap"}))

if __name__ == "__main__":
    main()