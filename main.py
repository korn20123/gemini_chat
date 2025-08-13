import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
history = []
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
  history.append(types.Content(role='user', parts=[types.Part(text=prompt)]))
  try:
    response = client.models.generate_content(
      model = 'gemini-2.0-flash',
      contents = history
    )
    reply = response.candidates[0].content.parts[0].text
    history.append(types.Content(role="model", parts=[types.Part(text=reply)]))
    return reply
  except Exception as e:
    print(e)
if __name__ == '__main__':
  main()