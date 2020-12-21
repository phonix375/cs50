import sys
import cs50
import csv
import re

# function to check how many times an siquance is in a string


def countCon(sqs, string):
    locations = [0]
    hightst = 0
    i = 1
    if len(([m.start() for m in re.finditer(sqs, string)])) == 0:
        return 0
    while True:
        locations = ([m.start() for m in re.finditer(sqs*i, string)])
        if len(locations) == 0:
            break
        i += 1
    return i-1


# check to see if the number of arguments is correct
if len(sys.argv) > 3:
    print("you did't supply the correct amount of arguments")
dataBase = []
seq = []
res = {}
# open an CSVf file and read it
with open(sys.argv[1], 'r') as file:
    aslist = csv.reader(file)
    for row in aslist:
        seq.append(row)
with open(sys.argv[1], 'r') as file:
    readers = csv.DictReader(file)
    for row in readers:
        dataBase.append(dict(row))

foo = open(sys.argv[2], 'r')
client = foo.read()
foo.close()
seq = seq[0][1:len(seq[0])]
for i in seq:
    res[i] = countCon(i, client)
found = False
# going over the databace to check if there is a match
for i in dataBase:
    match = 0
    for y in seq:
        if str(i[y]) == str(res[y]):
            match += 1

    if match == len(seq):
        print(i['name'])
        found = True
if not found:
    print("No match")