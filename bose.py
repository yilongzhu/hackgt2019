import requests

def setvol(vol):
    # set the params:
    ip = "192.168.137.100:8090"

    # form and send the /volume POST request
    xml = """
    <?xml version="1.0" ?>
    <volume>""" + str(vol) + """</volume>
    """
    send = requests.post('http://' + ip + '/volume', data=xml)

def skip():
    # set the params:
    ip = "192.168.137.100:8090"

    # form and send the /volume POST request
    xml = """
    <?xml version="1.0" ?>
    <key state="press" sender="Gabbo">"""
    + 'NEXT_TRACK'
    """</key>
    """
    send = requests.post('http://' + ip + '/key', data=xml)







if (command == 'setvol'):
            bose.setvol(params[1])
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

    