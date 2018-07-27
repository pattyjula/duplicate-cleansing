'''
DESC: Creates a CSV file of duplicate records
CAUTION: User must update CSV files and key_field values
AUTHOR: Patty Jula
DATE: July 2018
'''

from __future__ import print_function
import sys
from datetime import datetime
import pandas as pd

# Print start time
print("Start time: " + str(datetime.now()))
# Set variables
basepath= 'C:/Users/N5875/userOpenData/'
file_in = basepath +"input/CFS_2018.csv"
file_out = basepath + 'output/CFS_dupes.csv'
# key field value
field_name ="Incident_Number"
# read in CSV
df = pd.read_csv(file_in)
key_field = set(df[field_name].values)
header = True
print(len(df))

try:

    ids = df[field_name]
    data = pd.concat(g for _, g in df.groupby(field_name) if len(g) > 1) 
    print(len(data))
    if len(data) > 1:
        data.to_csv(file_out, mode='w', header=header, index=False)
        #header = False

    else:
        pass

    print("End time: " + str(datetime.now()))

except:
    # print error if there's a problem
    print("Unexpected error:", sys.exc_info()[0])
    raise