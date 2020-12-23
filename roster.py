import sys
import cs50
import csv

# main function


stud = []
# make sure there is another argument in argV
if len(sys.argv) < 2:
    print("please provide a hous name to show")
# open the database
db = cs50.SQL("sqlite:///students.db")
house = sys.argv[1]
res = (db.execute(r"SELECT * FROM students WHERE house = '%s' ORDER BY LAST, FIRST" % house))
for i in res:
    if i['middle'] != None:
        print("{} {} {}, born {}".format(i['FIRST'], i['middle'], i['LAST'], i['birth']))
    else:
        print("{} {}, born {}".format(i['FIRST'], i['LAST'], i['birth']))


# run the main function
