import csv
import glob
import os
import pandas as pd



def OpenFile(filename):
    with open(filename,'rb') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
    return data

def WriteFile(filename, data):
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

def ChangeHeader(data):
    for i in range(0,len(data[0])):
        print "looking at:" + data[0][i]
        if data[0][i] in ["TEMP_BOT", "BOT_TEMP", "BOTTEMP", 'TEMPBOTTOM', 'BOTTOMTEMP']:
            data[0][i] = 'BOT_TEMP'
            print "change at:" + str(i)
        elif data[0][i] in ["DATETIME", "DATE"]:
            data[0][i] = "DATETIME"
            print "change at:" + str(i)
        elif data[0][i] == "StratumCode":
            data[0][i] = 'STRATUM'
            print "change at:" + str(i)
        elif data[0][i] in ['scientific', 'SCINAME', 'SPECISSCIENTIFICNAME']:
            data[0][i] = 'SCIENTIFIC'
            print "change at:" + str(i)
        else:
            continue

def add_sources(data):
    data = [x + ['RUTGERS'] for x in data]
    return data


base_path = 'C:/Users/jialis/Documents/fish_data _2/'

for filename in os.listdir(base_path):
    if '.csv' in filename:
        full_filename = base_path + filename
        print "Searching file: " + full_filename
        data = OpenFile(full_filename)
        ChangeHeader(data)
        out_file = base_path + '/out/' + filename
        data = add_sources(data)
        WriteFile(out_file, data)
