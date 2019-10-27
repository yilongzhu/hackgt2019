import os
from flask import Flask, request
import dotenv

import bose
from gtts import gTTS

DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(DOTENV_PATH)
VERIFICATION_TOKEN = os.environ['VERIFICATION_TOKEN']

app = Flask(__name__)

@app.route('/tts', methods=['GET', 'POST'])
def tts():
    if request.form['token'] == VERIFICATION_TOKEN:
        payload = {'text': 'Slack slash command is successful!'}
        text = request.form['text']
        tts = gTTS(text=text, lang='en')
        tts.save("static/tts.mp3")

        bose.tts()
    else:
        payload = {'text': 'Invalid Request'}
    return payload

@app.route('/boost', methods=['GET', 'POST'])
def boost():
    if request.form['token'] == VERIFICATION_TOKEN:
        payload = {'text': 'Slack slash command is successful!'}
        text = request.form['text']
        user = request.form['user_name']
        channel = request.form['channel_name']
        params = text.split(" ")
        command = params[0]

        if (command == 'setvol'):
            #TODO: setvol function POST:/volume
            if (len(params) > 1):
                level = params[1]
                bose.setvol(level)
                payload['text'] = "Volume turned to " + level
            else:
                payload['text'] = "Please choose a volume level between 0 and 100"
        elif (command == 'info'):
            payload['text'] = bose.sinfo()
        elif (command == 'play'):
            payload['text'] = "Audio resumed"
            bose.play()
        elif (command == 'pause'):
            payload['text'] = "Audio paused"
            bose.pause()
        elif (command == 'skip'):
            bose.skip()
            payload['text'] = "Track skipped"
        elif (command in ["mute", "unmute"]):
            bose.mute()
            if(command=='mute'):
                payload['text'] = "Music muted"
            else:
                payload['text'] = "Music unmuted"
        elif (command == 'power'):
            try:
                status = bose.power()
                if (status == "STANDBY"):
                    payload['text'] = "Powered on"
                else:
                    payload['text'] = "Powered off"
            except:
                payload['text'] = "Power"
        elif (command == 'preset'):
            if (len(params) > 1):
                preset = params[1]
                bose.playpreset(preset)
                payload['text'] = "Now playing Preset " + preset
            else:
                payload['text'] = "Please choose a preset 1-6"
        else:
            return {'text': 'Invalid request'}
        return payload

    else:
        return {'text': 'Invalid request'}

if __name__ == '__main__':
    app.run()
