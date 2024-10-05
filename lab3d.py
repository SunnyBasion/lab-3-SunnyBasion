#!/usr/bin/env python3 
#Author mbasion | 107827172
import subprocess

def free_space():
    child_prcoess = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output = child_prcoess.communicate() 
    return output[0].decode('utf-8').strip()

if __name__ == '__main__':
    storage = free_space()
    print (storage)
