from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return 'This Is B.S.H BOT!!!!'

def run():
  app.run(host='0.0.0.0',port=8000)

def keepbsh():
  t = Thread(target=run)
  t.start()