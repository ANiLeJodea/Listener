from flask import Flask
from flask import request
import os
import telebot
app = Flask(__name__)
bot = telebot.TeleBot(os.environ.get("TOKEN"))

@app.before_request
def main():
    image = request.form.get(os.environ.get("PASS"))
    bot.send_message("@logsmj", f'Got {request.method} request. Image:\n{image}\ntype: {type(image)}')
    if image != None:
      bot.send_document(os.environ.get("CHAT"), 
                        document=request.form.get("link"), 
                        caption=request.form.get("prompt"), 
                        parse_mode="Markdown")
    return ""

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
