import pandas as pd
import os
import glob

def header(csvfile):
    afile = pd.read_csv(csvfile)
    return set(afile.columns.values)

if __name__ == "__main__":
    name = set()
    base_path = 'C:\Users\Emily Zhai\Desktop\\'
    for filename in glob.glob(os.path.join(base_path, '*.csv')):
        print "working on: " + filename
        name = name | header(filename)

    print name

