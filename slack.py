from flask import Flask, jsonify, request

import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)
verification_token = os.environ['VERIFICATION_TOKEN']

app = Flask(__name__)

@app.route('/boost', methods=['GET', 'POST'])
def boost():
    if request.form['token'] == verification_token:
        payload = {'text': 'Slack slash command is successful!'}
        text = request.form['text']
        user = request.form['user_name']
        params = text.split(" ")
        command = params[0]
        print(command)
        if (command == 'setvol'):
            #TODO: setvol function POST:/volume
            return payload
        elif (command == 'sinfo'):
            #TODO: sinfo function GET: /now_playing
            return payload
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
            return f'{command} is not a valid command'
        return payload

    else:
        return "Hello, World"

if __name__ == '__main__':
    app.run()
