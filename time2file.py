import time

def timeStamped(fmt='%H:%M:%S'):
    return time.strftime(fmt).format()

with open('../time.txt','w') as outf:
    outf.write(timeStamped())