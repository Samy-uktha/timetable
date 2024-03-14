import csv
with open("02_UG_CE_TimeTable_Jan-May-2024.xlsx - s2,s4.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

btech = {}
for sem in ('II','IV','VI','VIII'):
            btech[f"Semester_{sem}"] = {}    
            for branch in ['CE','CSE','EE','ME','DSE']:
                btech[f"Semester_{sem}"][branch] = {}


def getData(s, b):
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

    for semester in semesterList:
        for i in range(len(courseCodes)):
            courseCodes[i][0:2] = branch
            btech[f"Semester_{semester}"][branch][courseCodes[i]] = [courseNames[i],classes[i],labs[i]]
            