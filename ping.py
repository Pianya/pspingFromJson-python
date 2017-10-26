import json
from pprint import pprint
import os
import platform

dir = 'D:\Program files Portable\Shadowsocks'

with open (dir + '\gui-config.json') as data_file:
    data = json.load(data_file)

index = data["index"]
pprint(index)
i = 1
ip = data["configs"][i]["server"]
port = str(data["configs"][i]["server_port"])
#pprint(ip + ':' + port)
os.system('psping -t ' + ip + ':' + port)
