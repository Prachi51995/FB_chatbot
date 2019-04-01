
# coding: utf-8

# In[4]:


#Python libraries that we need to import for our bot
import os,sys
import random
from flask import Flask, request
from pymessenger.bot import Bot

ACCESS_TOKEN = "EAAE8ZAyVXw6cBAK0p2q3yFYmad8XuhRAbu3fWLY6xv702MqT0Cbp1flRVOhEdJfcSH3fBwS2hBRigbYSUOSrY0FYOrgMckbj96mmHSsVKbwvTb9yJCl1g460BcJU2P4XAps4rRtPLkDK6hwAaj3pIlZCvZC8OQIGAEz119ytwZDZD" ##ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
bot = Bot(ACCESS_TOKEN)

# In[ ]:


app = Flask(__name__)
@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)
    
    if data['object'] == "page":
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                
                #IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']
                
                if messaging_event.get('message'):
                    # HANDLE NORMAL MESSAGES HERE
                    if messaging_event.get('message'):
                        if 'text' in messaging_event['message']:
                            messaging_text = messaging_event['message']['text']
                        else:
                            messaging_text = 'no text'
                            
                        #Echo
                        response = messaging_text
                        bot.send_text_message(sender_id,response)

    return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug = True, port = 80)

