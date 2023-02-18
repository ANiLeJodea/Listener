from flask import Flask
from flask import request
import os
import telebot
app = Flask(__name__)
bot = telebot.TeleBot(os.environ.get("TOKEN"))


@app.before_request
def main():
    if request.form.get(os.environ.get("PASS")) != None:
        link = request.form.get("link")
        prompt = request.form.get("prompt")
        bot.send_document(request.form.get("user"),
                          document=link,
                          caption=prompt,
                          parse_mode="Markdown")
        bot.send_document(os.environ.get("USERNAME"),
                          document=link,
                          caption=prompt,
                          parse_mode="Markdown")
    return ""


app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
