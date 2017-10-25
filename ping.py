import json
from pprint import pprint

dir = 'D:\Program files Portable\Shadowsocks'

with open (dir + '\gui-config.json') as data_file:
    data = json.load(data_file)

test = data["configs"][0]["server"]

ping(test)

pprint(test)