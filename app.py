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
    return f"The api is running on {IPAddr}"

@app.route('/octo-hook', methods=['POST'])
def post_colour_change():
    audio = Audio()
    printer = request.json['deviceIdentifier']
    default_topic = f'_{request.json['topic'].replace(" ", "_")}'
    topic = f'{printer}_{request.json['topic'].replace(" ", "_")}'
    message = f'{printer} {request.json['message']}'
    audio_file = f"./audio/{topic}.wav"
    if not os.path.exists(audio_file):
        key = os.getenv('DEEPGRAM_API_KEY')
        if(key is not None and key != ""):
            with open('config.json') as config_file:
                config = json.load(config_file)
            if config['greeting'] is None:
                config['greeting'] = "Hello, your OctoPi Webhooks are ready!"
            if config['voice'] is None:
                config['voice'] = "aura-asteria-en"
            if config['device'] is None:
                config['device'] = 1
            print(json.dumps(config, indent=4))            
            deepgramAssistant = DeepgramAssistant(voice=config['voice'])        
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

if __name__ == '__main__':
    app.run(debug=True)