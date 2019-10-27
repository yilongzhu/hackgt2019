import requests

# set the params:
ip = "192.168.137.100:8090"

def setvol(vol):

    # form and send the /volume POST request
    xml = """
    <?xml version="1.0" ?>
    <volume>""" + str(vol) + """</volume>
    """
    send = requests.post('http://' + ip + '/volume', data=xml)

