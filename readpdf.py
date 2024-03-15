
import csv
with open("02_UG_CE_TimeTable_Jan-May-2024.xlsx - s2,s4.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

# for row in data_list:
#     print(row)

string = str(data_list[2])
s1 = [s.strip() for s in string.split(",")]
s2 = [s.strip() for s in s1[1].split(" ")]
if len(s2) == 2:
    semester = list(s2[1])
elif len(s2) == 4:
    sem = s2[1]
    semester = [sem]
    semester.append(s2[3])
newsem = []
for sem in semester:
    sem = "".join(c for c in sem if c.isalpha())
    newsem.append(sem)
semesterList = newsem
# print(semesterList)

reduced_data = []
for i in range(5,len(data_list)):
    reduced_data.append(data_list[i])
courseCodes = []
courseNames = []   
classSlots = []
labSlots = []
for r in reduced_data:
    courseCodes.append(r[0])
    courseNames.append(r[1])
    classSlots.append(r[6])
classes = []
labs = []
for c in classSlots:
     l = [s.strip() for s in c.split(",")]
     classes.append(l[0])
     labs.append(l[1])

# print(classes)
# print(labs)

btech = {}
for sem in ('II','IV','VI','VIII'):
    # for s in semesterList:
    #     if s == sem:
            btech[f"Semester_{sem}"] = {}    
            for branch in ['CE','CSE','EE','ME','DSE']:
                btech[f"Semester_{sem}"][branch] = {}
                for s in semesterList:
                    if s == sem:
                        for i in range(len(courseCodes)):
                            if courseCodes[i][0:2] == branch:
                                btech[f"Semester_{s}"][branch][courseCodes[i]] = [courseNames[i],classes[i],labs[i]]


for batch, branches in btech.items():
    print(batch)
    for branch in branches:
        print(f"  - {branch}: {btech[batch][branch]}")


#gjfgjjdigjfkgjdkgjdkfgj
        

