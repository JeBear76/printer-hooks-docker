import os
import socket
import json
from flask import Flask, request
from audio import Audio
from deepgramCommunication import DeepgramAssistant

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    audio = Audio()
    audio.play("greet.wav")
    hostname = socket.gethostname()
    print(hostname)
    IPAddr = socket.gethostbyname_ex(hostname)    
    return f"Hello, your OctoPi Webhooks are ready! <BR/> IP Address: {IPAddr[2][0]} <BR/> Use the URL: <a href='http://{os.getenv('HOST_NAME')}/octo-hook'>'http://{os.getenv('HOST_NAME')}/octo-hook'</a> in OctoPrint Webhooks"

@app.route('/octo-hook', methods=['POST'])
def octo_hook():
    audio = Audio()
    try:
        voice = request.json['voice']
        if(voice is None and voice == ""):
            voice = get_voice()
    except:
        voice = get_voice()
    printer = request.json['deviceIdentifier']
    default_topic = f'_{request.json['topic'].replace(" ", "_")}'
    topic = f'{printer}_{request.json['topic'].replace(" ", "_")}_{voice.split("-")[1]}'
    message = f'{printer} {request.json['message']}'
    audio_file = f"./audio/{topic}.wav"
    if not os.path.exists(audio_file):        
        key = os.getenv('DEEPGRAM_API_KEY')
        if(key is not None and key != ""):           
            deepgramAssistant = DeepgramAssistant(voice=voice, key=key)        
            deepgramAssistant.speak(message, audio_file)
        else:
            audio_file = f"{default_topic}.wav"            
    audio.play(audio_file)

    try:   
        if audio is not None:
            del audio
    except:
        pass
    try:   
        if deepgramAssistant is not None:
            del deepgramAssistant
    except:
        pass
    
    return f'''{{
                "status": "success",
                "message": "Webhook processed successfully"
            }}'''

def get_voice():
    with open('config.json') as config_file:
        config = json.load(config_file)
        if config['voice'] is None or config['voice'] == "":
            return "aura-helios-en"
        return config['voice']

if __name__ == '__main__':
    app.run(debug=True)