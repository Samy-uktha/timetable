import csv

btechCSV = [
    [
        "csv files/01_UG_CommonCourses_TimeTable_Jan-May-2024.xlsx - S2.csv",
        "csv files/01_UG_CommonCourses_TimeTable_Jan-May-2024.xlsx - S2, S4 SME.csv",
        "csv files/01_UG_CommonCourses_TimeTable_Jan-May-2024.xlsx - HSE.csv",
        "csv files/01_UG_CommonCourses_TimeTable_Jan-May-2024.xlsx - GCE.csv"

    ],
    [
        "csv files/02_UG_CE_TimeTable_Jan-May-2024.xlsx - s2,s4.csv",
        "csv files/02_UG_CE_TimeTable_Jan-May-2024.xlsx - s6.csv",
        "csv files/02_UG_CE_TimeTable_Jan-May-2024.xlsx - s8.csv",
        "csv files/02_UG_CE_TimeTable_Jan-May-2024.xlsx - PME_ERC.csv"
    ],
    [
        "csv files/03_UG_CSE_TimeTable_Jan-May-2024.xlsx - s2,s4.csv",
        "csv files/03_UG_CSE_TimeTable_Jan-May-2024.xlsx - s6.csv",
        "csv files/03_UG_CSE_TimeTable_Jan-May-2024.xlsx - s8.csv",
        "csv files/03_UG_CSE_TimeTable_Jan-May-2024.xlsx - PME_ERC.csv"
    ],
    [
        "csv files/05_UG_EE_TimeTable_Jan-May-2024.xlsx - s2,s4.csv",
        "csv files/05_UG_EE_TimeTable_Jan-May-2024.xlsx - s6.csv",
        "csv files/05_UG_EE_TimeTable_Jan-May-2024.xlsx - s8.csv",
        "csv files/05_UG_EE_TimeTable_Jan-May-2024.xlsx - PME_ERC.csv"
    ],
    [
        "csv files/06_UG_ME_TimeTable_Jan-May-2024.xlsx - s2,s4.csv",
        "csv files/06_UG_ME_TimeTable_Jan-May-2024.xlsx - s6.csv",
        "csv files/06_UG_ME_TimeTable_Jan-May-2024.xlsx - s8.csv",
        "csv files/06_UG_ME_TimeTable_Jan-May-2024.xlsx - PME_ERC.csv"
    ],
    [
        "csv files/04_UG_DS_TimeTable_Jan-May-2024.xlsx - s2,s4.csv"
    ]
]

branchnumber = {
    "CE": "02",
    "CSE": '03',
    "DS": '04',
    "EE": '05',
    "ME": '06'
}

def getBtechData(sem,branch):
    core_list = []
    sme_list = []
    hse_list = []
    dictarray = {}
    # courses = []
    bnum = branchnumber[branch]
    if sem in [6,8]:
        with open(f"csv files/{bnum}_UG_{branch}_TimeTable_Jan-May-2024.xlsx - s{sem}.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                core_list.append(row)
    elif sem == 4:
        with open(f"csv files/{bnum}_UG_{branch}_TimeTable_Jan-May-2024.xlsx - s2,s4.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                core_list.append(row)
        with open("csv files/01_UG_CommonCourses_TimeTable_Jan-May-2024.xlsx - S2, S4 SME.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                sme_list.append(row)
        with open("csv files/01_UG_CommonCourses_TimeTable_Jan-May-2024.xlsx - HSE.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                hse_list.append(row)
        
        
    elif sem == 2:
        with open("csv files/01_UG_CommonCourses_TimeTable_Jan-May-2024.xlsx - S2.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                core_list.append(row)
    reduced_core = []
    reduced_sme = []
    reduced_hse = []
    for i in range(5,len(core_list)):
        reduced_core.append(core_list[i])
    for i in range(5,len(sme_list)):
        reduced_sme.append(sme_list[i])
    for i in range(5,len(hse_list)):
        reduced_hse.append(hse_list[i])
    # print(sme_list)
    # print(reduced_sme)
    def getList(data):
        courses = []
        courseCodes = []
        courseNames = []   
        classSlots = []
        for r in data:
            courseCodes.append(r[0])
            courseNames.append(r[1])
            classSlots.append(r[6])
        classes = []
        labs = []
        for c in classSlots:
            l = [s.strip() for s in str(c).split(",")]
            classes.append(l[0])
            if len(l)>1:
                labs.append(l[1])
            else:
                labs.append(0)
        for i in range(len(courseCodes)):
            if courseCodes[i] == '':
                break
            elif not courseCodes[i][0].isalpha():
                break
            courses.append([courseCodes[i],courseNames[i],classes[i],labs[i]])
        return courses
    
    # print(courses)
    dictarray["CORE"] = getList(reduced_core)
    dictarray["SME"] = getList(reduced_sme)
    dictarray["HSE"] = getList(reduced_hse)
    # courses = []
    # for dic in dictarray:
    #     for key in dic:
    #         if key == '':
    #             break
            #if key != '':
            # if str(key)[0].isalpha():
            #     courses.append(dic)
            # if [k.isalpha() for k in key]:
            #     print(k)
            #     courses.append(dic)
    
    return dictarray
    
d = getBtechData(4,"CSE")
for key, value in d.items():
    print(key,"-")
    for v in value:
        print(v)
# print(d)
                