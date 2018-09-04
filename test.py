
import csv
uw = open("Date.txt", "r")
for row1 in csv.DictReader(uw, ["usr_id", "usr_weight"]):
    print( row1["usr_id"],row1["usr_weight"])