import pandas as pd
import os 
import sys
import time
import json

## Bring in data
data = pd.read_json('https://healthdata.gov/resource/vbjv-rh5z.json')
data

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

## get current time
now = time.time()

## Save time as string
cTime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print(cTime)

data.to_csv('Data/Social_Determinants_and_Health_Equity_Resource_Guide.csv')

# create a new file in the current working directory
with open(cwd + '/testFile_' + cTime + '.txt', 'w') as f:
    f.write(str(data))
