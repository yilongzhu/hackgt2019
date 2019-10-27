import requests
import xml.etree.ElementTree as ET

# set the params:
ip = "192.168.137.139:8090"

def setvol(vol):

    # form and send the /volume POST request
    xml = """
    <?xml version="1.0" ?>
    <volume>""" + str(vol) + """</volume>
    """
    send = requests.post('http://' + ip + '/volume', data=xml)

def skip():

    # form and send the /volume POST request
    xml = """
    <?xml version="1.0" ?>
    <key state="press" sender="Gabbo">NEXT_TRACK</key>
    """
    send = requests.post('http://' + ip + '/key', data=xml)

def sinfo():
    response = requests.get('http://' + ip + '/now_playing')
    root = ET.fromstring(response.content)
    source_context = root.find("ContentItem").attrib
    media_player = source_context["source"]
    track = root.find("track").text
    artist = root.find("artist").text
    album = root.find("album").text
    cover = root.find("art").text
    metadata = "Playing from " + media_player + ":\nTrack: " + track + "\nArtist: " + artist + "\nAlbum: " + album + "\n" + cover
    return metadata

def play():
    xml = """
    <?xml version="1.0" ?>
    <key state="press" sender="Gabbo">PLAY</key>
    """
    send = requests.post('http://' + ip + '/key', data=xml)

def pause():
    xml = """
    <?xml version="1.0" ?>
    <key state="press" sender="Gabbo">PAUSE</key>
    """
    send = requests.post('http://' + ip + '/key', data=xml)

def power():
    response = requests.get('http://' + ip + '/now_playing')
    root = ET.fromstring(response.content)
    source_context = root.attrib
    print(source_context)
    xml = """
    <?xml version="1.0" ?>
    <key state="press" sender="Gabbo">POWER</key>
    """
    send = requests.post('http://' + ip + '/key', data=xml)
    xml = """
    <?xml version="1.0" ?>
    <key state="release" sender="Gabbo">POWER</key>
    """
    send = requests.post('http://' + ip + '/key', data=xml)
    return source_context['source']

def mute():
    # form and send the /volume POST request
    xml = """
    <?xml version="1.0" ?>
    <key state="press" sender="Gabbo">MUTE</key>
    """
    send = requests.post('http://' + ip + '/key', data=xml)

def playpreset(num):
    xml = """
    <?xml version="1.0" ?>
    <key state="release" sender="Gabbo">PRESET_"""+str(num)+"""</key>
    """
    send = requests.post('http://' + ip + '/key', data=xml)

def tts():
    xml = """
    <?xml version="1.0" ?>
    <play_info>
        <app_key>Zox8jYe4gMWQf2LYwoXIsq9QVDe7goPm</app_key>
        <url>https://hackgt2019.yilongzhu.com/static/tts.mp3</url>
        <service>TTS</service>
        <volume>70</volume>
    </play_info>
    """
    send = requests.post('http://' + ip + '/speaker', data=xml)
