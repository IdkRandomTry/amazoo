# This is ctrl c ctrl v...
from flask import Flask
from threading import Thread
import random
import time
import requests
import logging
app = Flask('')
@app.route('/')
def home():
    return "doffjrdj i,stkrr"

def run():
  app.run(host='0.0.0.0',port=random.randint(2000,9000)) 
def ping(target, debug):
    while(True):
        r = requests.get(target)
        if(debug == True):
            print("Status Code: " + str(r.status_code))
        time.sleep(300) 
def awake(target, debug=False):  
    log = logging.getLogger('werkzeug')
    log.disabled = True
    app.logger.disabled = True  
    t = Thread(target=run)
    r = Thread(target=ping, args=(target,debug,))
    t.start()
    r.start()

'''from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Discord.py Bot is online"
    
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()'''