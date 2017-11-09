import json
from pprint import pprint
import os
import platform
import concurrent.futures

# function of call psping and miscellous
def f(i):
    ip = data["configs"][i]["server"]
    port = str(data["configs"][i]["server_port"])
    remark = data["configs"][i]["remarks"]
    res = os.popen('psping -q -i 0 ' + ip + ':' + port + ' -nobanner').read()
    print('request for server ' + remark + '\n' + res)
# main function    
def main():
    # ask for dir: gui-config.json
    dir = input('Enter the dir: ')
    # load json
    with open (dir) as data_file:
        data = json.load(data_file)
    # count no. of servers
    count = len(data['configs'])
    pprint(count)
    # psping each server
    # lets try concurrent calling
    # ThreadPool:
    #with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    #   for i in range (0,count):
    #        executor.submit(f,i)
    # ProcessPool:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in zip(range(0,count),executor.map(f,range(0,count)))
        
if __name__ == '__main__':
    main()