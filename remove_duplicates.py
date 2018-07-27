'''
DESC: Remove duplicates from file_in
CAUTION: User must update CSV files and key_field values
AUTHOR: Patty Jula
DATE: July 2018
'''
from __future__ import print_function
import sys
from datetime import datetime
import time
import pandas as pd
import csv
from pathlib import Path

print("Start time: " + str(datetime.now()))
timestr = time.strftime("%Y%m%d")
basepath= 'C:/Users/user/OpenData'
file_in = basepath + '/input/' + "CFS_2018.csv"


try:
    # Read in CSV
    df= pd.read_csv(file_in)

    # Check if duplicate file is found
    # before running to make clean file
    file_out2 = Path(basepath + '/output/' + 'CFS_dupes.csv')
    if file_out2.is_file():
        print("Duplicates found")
        file_out = basepath + '/output/' + 'CFS_clean.csv'
        with open(file_in, 'r') as fin, open(file_out, 'w', newline='') as fout:
            reader = csv.reader(fin)
            writer = csv.writer(fout)
            d = {}
            for row in reader:
                DR = row[0]
                if DR not in d:
                    d[DR] = row
                    writer.writerow(row)
                elif DR in d:
                    continue
                else:
                    continue
        result = d.values()
        df= pd.read_csv(file_out)
        
        print('Clean output CSV count:',len(df))
    else:
        print("No duplicates found")
        pass

except:
    # print error if there's a problem
    print("Unexpected error:", sys.exc_info()[0])
    raise