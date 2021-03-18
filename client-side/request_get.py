import requests
import json
import string
import random

#Generate random string to complete Acknowledge
def random_string(length):
    random_list = []
    for i in range(length):
        random_list.append(random.choice(string.ascii_uppercase + string.digits))
    print("ACK    :",''.join(random_list))
    return ''.join(random_list)

#Data going to send
key = 'bd2722b3-955e-4261-b135-183283cd5515'
d1 = 10
d2 = 10.5
d3 = -9
d4 = -5.4
ack = random_string(19)

#Send data through GET Method
def main(key, d1, d2, d3, d4, ack):
    url = "http://127.0.0.1:5199/data/data.json?key="+key+"&d1="+str(d1)+"&d2="+str(d2)+"&d3="+str(d3)+"&d4="+str(d4)+"&ack="+ack
    print("URL    :",url)
    result = requests.get(url)
    print("Result :",result)
    return (result)

main(key, d1, d2, d3, d4, ack)
