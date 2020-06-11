import pandas as pd
import itertools
import collections
import numpy
from prettytable import PrettyTable
import csv

url="https://docs.google.com/spreadsheets/d/e/2PACX-1vTGdH3omi_WopqjlWg44qd2Kf_bAwyzaIdYYiMj1cXGs5YH9Lqtbr-otNMA1DwHVrH917IQ5aB-Vvra/pub?gid=1373322240&single=true&output=csv"

# Create a dataframe from csv
df = pd.read_csv(url, delimiter=',',header=1, usecols=range(2,11))
#df = pd.read_csv('seker2.csv', delimiter=',',header=1, usecols=range(2,11),  dtype={"Timestamp": str,"מייל טכניוני":str , "מספר קורס 1": str, "מספר קורס 2": str,"מספר קורס 3": str,"מספר קורס 4": str,"מספר קורס 5": str,"מספר קורס 6": str,"מספר קורס 7": str,"מספר קורס 8": str,"מספר קורס 9": str,"מספר קורס 10": str})
df.replace("", numpy.nan, inplace=True)
# User list comprehension to create a list of lists from Dataframe rows
list_of_rows = [list(row) for row in df.values]
# Insert Column names as first list in list of lists
list_of_rows.insert(0, df.columns.to_list())

# Print list of lists i.e. rows
#print(list_of_rows)


a=list_of_rows

counts = collections.defaultdict(int)

converted = [[str(num) for num in sub] for sub in a]
#print (converted)
for collab in converted:
    collab.sort()
    for cell in collab:
        #cell=(cell).split(".", 1)[0]
        cell=cell.split(".", 1)[0]
        if "Unnamed" in str(cell):
            cell=""
        if "nan" in str(cell):
            cell=""
        '''elif type(cell)==numpy.float64:
                    #print(pair)
                    cell=cell.split(".", 1)[0]
        else:
            cell=str(cell).split(".", 1)[0]'''

    for pair in itertools.combinations_with_replacement(collab, 2):

        if "Unnamed" in str(pair):
            continue
        if "nan" in str(pair):
            continue
        counts[pair] += 1


#print(counts.items())
for i in counts.items():
        #cell=(cell).split(".", 1)[0]
        i=str(i[1]).strip().replace(".0","")

new_l={k: v for k, v in sorted(counts.items(), key=lambda item: item[1],reverse=True)}
results=PrettyTable(['Course 1','Course 2', 'Intersections'])
for pair, freq in new_l.items():
    if pair[0]==pair[1]:
        #print(pair[0],"and ", pair[1])
        continue
    if freq>1:
        results.add_row([pair[0].replace(".0",""),pair[1].replace(".0",""), freq])

print(results)


