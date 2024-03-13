# import pandas as pd
# data = pd.read_csv("02_UG_CE_TimeTable_Jan-May-2024.xlsx - s2,s4.csv")
# codes = data["5"]
# # print(data[0][4])
# print(codes)

# # for d in data : 
# #     print(d)

# Open the CSV file for reading
import csv

# Open the CSV file for reading
with open("02_UG_CE_TimeTable_Jan-May-2024.xlsx - s2,s4.csv", newline='') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)
    
    # Initialize an empty list to store the data
    data_list = []
    
    # Iterate over each row in the CSV file and append it to the data list
    for row in csv_reader:
        data_list.append(row)

for row in data_list:
    print(row)

string = str(data_list[2])
s1 = [s.strip() for s in string.split(",")]
s2 = [s.strip() for s in s1[1].split(" ")]
if len(s2) == 2:
    semester = s2[1]
elif len(s2) == 4:
    semester = list(s2[1])
    semester.append(s2[3])

for c in s2:
    if not c.isalpha():
        s11="".join(c)
#sem = "".join(c for c in sem if c.isalpha())
#print(semester)

reduced_data = []
# Print the list
for i in range(5,len(data_list)):
    reduced_data.append(data_list[i])
    
courseCodes = []
courseNames = []   
slots = []
rooms = [] 
for row in reduced_data:
    courseCodes.append(row[0])

