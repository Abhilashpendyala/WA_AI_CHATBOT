import requests
import openai
import json
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv("var.env")
first_message="hi"
token=os.getenv("token")

app=Flask(__name__)
url="https://graph.facebook.com/v22.0/798077006733009/messages"


payload={
    "messaging product":"whatsapp",
    "to":"918179784745",
    "type":"text",
    "text": {"body": first_message}
}

headers = {
    "Authorizatioin": "Bearer {token}",
    "Content-Type": "application/json"
}
requests.post(url=url,headers=headers,json=payload)
