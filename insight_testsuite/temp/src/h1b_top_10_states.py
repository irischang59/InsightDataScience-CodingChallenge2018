import sys  
import os
import numpy as np
import csv
import collections
import operator


# read in csv file and store data into array
list1 = []
with open(sys.argv[1]) as csvfile:
    f = csv.reader(csvfile, delimiter=';')
    for row in f:
        list1.append(row)
arr1 = np.asarray(list1)

# select 'CASE_STATUS' & 'WORKSITE_STATE' columns
arr2 = arr1[:,[2,50]]

# delete header
arr3 = np.delete(arr2, 0, 0)

# keep rows where 'CASE_STATUS' is 'CERTIFIED'
arr4 = arr3[np.where(arr3[:,0] == 'CERTIFIED')]

# define a function which returns a dictionary data structure whose keys are array elements and values are their corresponding frequencies
def CountFrequency(arr): 
    return collections.Counter(arr)

# count frequency of each occupation
freq = CountFrequency(arr4[:,1])

# total cases
total = np.size(arr3,0)

temp = []
dictList = []
# sort the values in descending order and the keys alphabetically in ascending order
for key, value in sorted(freq.iteritems(), key=lambda (k,v):(-v, k)):
    temp = [key,value]
    dictList.append(temp)

# define a function to calculate the percentage of certified applications
def percentage(a,b):
    return round(a/b*100,1)

# convert the percentage from float to string and add '%' symbol
for i in range(np.shape(dictList)[0]):
    dictList[i].append(str(percentage(float(dictList[i][1]),total))+ '%')

# create 'TOP_OCCUPATIONS' & 'NUMBER_CERTIFIED_APPLICATIONS' & 'PERCENTAGE' lists and write then into text files respectively
ls_1 = [item[0] for item in dictList]
ls_1_new = []
for item in ls_1:
    ls_1_new.append(item+";")
ls_1_new = "\n".join(map(lambda x: str(x), ls_1_new))

textfile1 = open('textfile4.txt', 'w')
textfile1.write(ls_1_new)
textfile1.close()

ls_2 = [item[1] for item in dictList]
ls_2_new = []
for item in ls_2:
    ls_2_new.append(str(item)+";")
ls_2_new = "\n".join(map(lambda x: str(x), ls_2_new))

textfile2 = open('textfile5.txt', 'w')
textfile2.write(ls_2_new)
textfile2.close()

ls_3 = [item[2] for item in dictList]
ls_3_new = []
for item in ls_3:
    ls_3_new.append(item)
ls_3_new = "\n".join(map(lambda x: str(x), ls_3_new))

textfile3 = open('textfile6.txt', 'w')
textfile3.write(ls_3_new)
textfile3.close()

# concatenate text files line by line and output the final text file to the desired directory
textfile1 = open("textfile4.txt", "r")
textfile2 = open("textfile5.txt", "r")
textfile3 = open("textfile6.txt", "r")

out = open(sys.argv[2], "w")
out.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
for line in textfile1:
    out.write(line.strip() + textfile2.readline().strip() + textfile3.readline().strip())
    out.write("\n")
out.close()

