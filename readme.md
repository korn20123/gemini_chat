# gemini_chat
## introduction
this small application was coded by me because i was bored.
it's a simple python chatbot that uses gemini.
## installation
first setup a virtual environment using this command:
```bash
python3 -m venv env
source env/Scripts/activate
```
note: you must have python installed for this.
then type:
```bash
pip install -r requirements.txt
```
then create an file named .env with that contents:
```dotenv
GEMINI_API_KEY=yourapikeyhere
```
note: replace yourapikeyhere with your gemini apikey. get at: https://aistudio.google.com/app/apikey 
and last: type:
```bash
python main.py
```
