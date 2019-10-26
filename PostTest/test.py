import requests
import xml.dom.minidom


# set the params:
ip = "192.168.137.160" # enter your speaker IP address here

# form and send the /speaker POST request
sendXML = '<key state="$KEY_STATE" sender="$KEY_SENDER">$PAUSE</key>'
send = requests.post('http://' + ip + '/speaker', data=sendXML)

# print a pretty version of the response - not required but can be helpful for reading errors if they occur
responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print(responseXML_pretty)
