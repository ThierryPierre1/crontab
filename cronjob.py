import pandas as pd
import os 
import sys
import time
import json

## Bring in data
data = pd.read_json('https://healthdata.gov/resource/vbjv-rh5z.json')
data

## get current time
now = time.time()
timestart = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This program started running at: ', timestart)

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)