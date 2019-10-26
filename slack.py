from flask import Flask, jsonify, request

import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)
verification_token = os.environ['VERIFICATION_TOKEN']

app = Flask(__name__)

@app.route('/boost', methods=['GET', 'POST'])
def boost():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
