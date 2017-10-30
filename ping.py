import json
from pprint import pprint
import os
import platform

dir = input('Enter the dir: ')

with open (dir) as data_file:
    data = json.load(data_file)

index = data["index"]
pprint(index)

def f(i):
    ip = data["configs"][i]["server"]
    port = str(data["configs"][i]["server_port"])
    remark = data["configs"][i]["remarks"]
    pprint('request for server ' + remark)
    os.system('psping -q -i 0 ' + ip + ':' + port + ' -nobanner')

for i in range (0,index):
    f(i)
    i = i + 1
