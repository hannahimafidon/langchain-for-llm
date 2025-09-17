## Outline
# Direct API calls to OpenAI
# API calls through LangChain: Prompts, Models, Output parsers

# pip install python-dotenv
# pip install openai

import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']