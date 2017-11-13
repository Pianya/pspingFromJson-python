import json
import os
import multiprocessing
import time

# profiler
def profile(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print ('COST: {}'.format(end - start))
    return wrapper

# function of call psping and miscellous
def f(i,data):
    ip = data["configs"][i]["server"]
    port = str(data["configs"][i]["server_port"])
    remark = data["configs"][i]["remarks"]
    res = os.popen('psping -q -i 0 ' + ip + ':' + port + ' -nobanner').read()
    print('request for server ' + remark + '\n' + res)

@profile
def notmultiprocess():
    for i in range(count):
        f(i,data)

@profile
def ismultiprocess():
    jobs = []
    for i in range(count):
        p = multiprocessing.Process(target=f,args=(i,data))
        p.start()
        jobs.append(p)

    for p in jobs:
        p.join()
    
# main function
if __name__ == '__main__':
    # ask for dir: gui-config.json
    dir = input('Enter the dir: ')
    # load json
    with open (dir) as data_file:
        data = json.load(data_file)
    # count no. of servers
    count = len(data['configs'])
    print(count)
    # psping each server, multiprocessing

    ismultiprocess()
    #notmultiprocess()