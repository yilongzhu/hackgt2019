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

setvol(30)
