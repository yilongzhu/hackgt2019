import os
from flask import Flask, request
import dotenv

import bose

DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(DOTENV_PATH)
VERIFICATION_TOKEN = os.environ['VERIFICATION_TOKEN']

app = Flask(__name__)

@app.route('/boost', methods=['GET', 'POST'])
def boost():
    if request.form['token'] == VERIFICATION_TOKEN:
        payload = {'text': 'Slack slash command is successful!'}
        text = request.form['text']
        user = request.form['user_name']
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
            payload['text'] = "Audio Resumed"
            bose.play()
        elif (command == 'pause'):
            payload['text'] = "Audio Paused"
            bose.pause()
        elif (command == 'skip'):
            bose.skip()
            payload['text'] = "Track skipped"
        elif (command == 'power'):
            status = bose.power()
            if (status == "STANDBY"):
                payload['text'] = "Powered on"
            else:
                payload['text'] = "Powered off"
        else:
            return {'text': 'Invalid request'}
        return payload

    else:
        return {'text': 'Invalid request'}

if __name__ == '__main__':
    app.run()
