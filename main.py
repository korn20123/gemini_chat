import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
def main():
  while True:
    prompt = input('you: ')
    if prompt.lower() == 'exit':
      break
    try:
      answer = send(prompt)
      print(answer)
    except Exception as e:
      print(e)
def send(prompt):
  try:
    response = client.models.generate_content(
      model = 'gemini-2.0-flash',
      contents = prompt
    )
    return response.text
  except Exception as e:
    print(e)
if __name__ == '__main__':
  main()