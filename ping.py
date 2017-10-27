import json
from pprint import pprint
import os
import platform


dir = input('Enter the dir: ')

with open (dir) as data_file:
    data = json.load(data_file)

index = data["index"]
pprint(index)

while (i < index):
	ip = data["configs"][i]["server"]
    port = str(data["configs"][i]["server_port"])
    remark = data["configs"][i]["remarks"]
    #pprint(ip + ':' + port)
    pprint('request for server ' + remark)
    os.system('psping -q -i 0 ' + ip + ':' + port)
    i = i + 1
