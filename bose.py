import requests
import xml.etree.ElementTree as ET

# set the params:
ip = "192.168.137.100:8090"

def setvol(vol):

    # form and send the /volume POST request
    xml = """
    <?xml version="1.0" ?>
    <volume>""" + str(vol) + """</volume>
    """
    send = requests.post('http://' + ip + '/volume', data=xml)

def sinfo():
    response = requests.get('http://' + ip + '/now_playing')
    root = ET.fromstring(response.content)
    source_context = root.find("ContentItem").attrib
    media_player = source_context["source"]
    track = root.find("track").text
    artist = root.find("artist").text
    album = root.find("album").text
    metadata = "Playing from " + media_player + ":\nTrack: " + track + "\nArtist: " + artist + "\nAlbum: " + album
    print(metadata)
    return metadata

