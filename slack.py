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
            #TODO: sinfo function GET: /now_playing
            return bose.sinfo()
        elif (command == 'play'):
            #TODO: presets function POST: /key state:press val: PLAY
            return payload
        elif (command == 'pause'):
            #TODO: pause function POST: /key state:press val: PAUSE
            return payload
        elif (command == 'skip'):
            #TODO: presets function POST: /key state:press val: NEXT_TRACK
            return payload
        elif (command == 'power'):
            #TODO: presets function POST: /key state:press val: POWER
            #TODO: presets function POST: /key state:release val: POWER
            return payload
        else:
            return {'text': 'Invalid request'}
        return payload

    else:
        return {'text': 'Invalid request'}

if __name__ == '__main__':
    app.run()
