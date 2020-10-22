from sys import stdout
from time import sleep

def Writer(s,z):
    sleep(0.3)
    for i in s + '\n':
        stdout.write(i)
        stdout.flush()
        sleep(z / 100)


    
