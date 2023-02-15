from flask import Flask
from flask import request
import os
import telebot
app = Flask(__name__)
bot = telebot.TeleBot(os.environ.get("TOKEN"))

@app.before_request
def main():
  image = request.form.get(os.environ.get("PASS"))
  if image != None:
      bot.send_photo(os.environ.get("CHAT"), image["link"], image["prompt"], "Markdown")

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))

