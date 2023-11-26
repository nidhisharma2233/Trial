
"""2. File I/O:
   - Understanding file handling in Python.
   - Reading, writing, and appending data to text files.
   - Handling different file formats like CSV, JSON."""


#file create through file handling

f = open("myfile.txt", "w")
f.write("hello i am nidhi")
f.write("file handling work")
f.close()
f = open("myfile.txt", "w")
f.write("hello i am khushi")
f.write("file handling task")
f.close()

#file read
f=open("myfile.txt",'r')
print(f.read())
print(f.readline(4))#specified word read

# append function
f = open("myfile.txt", "a")
f.write("hello i am nidhi")
f.close()

f.close()

import csv

with open('csvfile.csv', 'w',newline='') as file:
  writer = csv.writer(file)

  writer.writerow(["SNo", "Name", "Subject"])
  writer.writerow([1, "nidhi sharma", "English"])
  writer.writerow([2, "Gary Oak", "Mathematics"])
  writer.writerow([3, "Brock Lesner", "Physics"])
file.close()

#read
with open("csvfile.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)

  #print(file.readlines())
file.close()

#append
with open("csvfile.csv", 'a') as file:
  writer = csv.writer(file)
  writer.writerow([4, "crock Lesner", "hindi"])
file.close()

#write
import json
set1={'yes','amit','nisha','Anirudh','Pooja'}
with open('json_demo.json','w') as f:
  json.dump(set1,f)
f.close()

#read
with open('json_demo.json','r') as f:
  d=json.load(f)
  print(d)
f.close()

#append 
with open('json_demo.json','a') as f:
  json.dump(("hello","yes","me"),f)
f.close()










