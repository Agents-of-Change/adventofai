import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)

print(response.choices[0].text)
