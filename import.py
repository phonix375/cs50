import sys
import cs50
import csv


# this is the main function
def main():
    stud = []

    # check if user provided the correct number of arguments
    if len(sys.argv) < 2:
        print("please provide a file name to import")
        return 1
    # open the data base to write
    open(f"students.db", "w").close()
    db = cs50.SQL("sqlite:///students.db")
    db.execute("""

    CREATE TABLE students (
	id INTEGER PRIMARY KEY,
	first TEXT NOT NULL,
	middle TEXT,
	last TEXT,
	house TEXT,
	birth INTEGER
);

    """)
    # open the CSV file to load into the databse
    with open(sys.argv[1], "r") as stidents:
        reader = csv.DictReader(stidents)
        for row in reader:
            stud.append([row['name'], row['house'], row['birth']])
    # loop over the resoult
    for i in stud:
        if len(i[0].split()) > 2:
            x = i[0].split()[1]
        else:
            x = 'None'
        db.execute("""
            INSERT INTO students
            (first, middle, last, house, birth)
            VALUES(?, ?, ?, ?, ?)""",
                   i[0].split(" ")[0], x, i[0].split()[len(i[0].split())-1], i[1], i[2])


if __name__ == "__main__":
    main()