import csv

def getData(sem,branch):
    branchnumber = {
        "CE": "02",
        "CSE": '03',
        "DS": '04',
        "EE": '05',
        "ME": '06',
        "CY": "07", #MSc chemistry
        "MA": "08", #MSc math
        "PH": "09", #MSc physics
        "HSS": "10", #Humanities
        "CaM": "11", #Mtech omputing and Mathematics
        "DSPG": "12", #Mtech Data Science Post Grad
        "Geo": "13", #Mtech Geotechnical
        "MME": "14", #Mtech Manufacturing and Materials
        "PEPS": "15", #Mtech Power Electronics and Power Systems
        "SOCD": "16" #Mtech System on Chip Design
    }
    common_list = []
    core_list = []
    sme_list = []
    hse_list = []
    pme_list = []
    gce_list = []
    elective_list = []
    hrc_list = []
    dictarray = {}
    # courses = []
    bnum = branchnumber[branch]
    if branch in ["CE","CSE","EE","ME","DS"]:
        if sem in [6,8]:
            with open(f"csv files/{bnum}_UG_{branch}_TimeTable_Jan-May-2024.xlsx - s{sem}.csv", newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    core_list.append(row)
            with open(f"csv files/{bnum}_UG_{branch}_TimeTable_Jan-May-2024.xlsx - PME_ERC.csv", newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    pme_list.append(row)
            with open(f"csv files/01_UG_CommonCourses_TimeTable_Jan-May-2024.xlsx - GCE.csv", newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    gce_list.append(row)
        
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
            with open(f"csv files/01_UG_CommonCourses_TimeTable_Jan-May-2024.xlsx - GCE.csv", newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    gce_list.append(row)
        elif sem == 2:
            with open("csv files/01_UG_CommonCourses_TimeTable_Jan-May-2024.xlsx - S2.csv", newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    common_list.append(row)
    elif branch in ["CaM","DS","Geo","MME","PEPS","SOCD"]:
        with open(f"csv files/{bnum}_PG_Mtech_{branch}_TimeTable_Jan-May-2024.xlsx - s{sem}.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                core_list.append(row)
        with open(f"csv files/{bnum}_PG_Mtech_{branch}_TimeTable_Jan-May-2024.xlsx - PE_ERC.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                elective_list.append(row)
    elif branch in ["CY","PH"]:
        with open(f"csv files/{bnum}_PG_{branch}_TimeTable_Jan-May-2024.xlsx - s{sem}.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                core_list.append(row)
        with open(f"csv files/{bnum}_PG_{branch}_TimeTable_Jan-May-2024.xlsx - PSE_SRC.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                elective_list.append(row)
    elif branch == "MA":
        with open(f"csv files/{bnum}_PG_{branch}_TimeTable_Jan-May-2024.xlsx - s{sem}.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                core_list.append(row)
    elif branch == "HSS":
        with open(f"csv files/10_PG_HSS_TimeTable_Jan-May-2024.xlsx - HRC.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                hrc_list.append(row)
    elif branch == "DSPG":
        with open(f"csv files/12_PG_MTech_DS_TimeTable_Jan-May-2024.xlsx - s2.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                core_list.append(row)
        with open(f"csv files/12_PG_MTech_DS_TimeTable_Jan-May-2024.xlsx - PE_ERC.csv", newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                elective_list.append(row)
    
    def getList(d):
        data = []
        # for i in range(5,len(d)):
        #     data.append(d[i])

        courses = []
        courseCodes = []
        courseNames = []   
        classSlots = []

        if d is common_list:
            for i in range(4,len(d)):
                data.append(d[i])
            for i in range(len(data)):
                r = data[i]
                if r[0]:
                    courseCodes.append(r[0])
                    courseNames.append(r[1])
                    classSlots.append(r[4])
        else:
            for i in range(5,len(d)):
                data.append(d[i])
            for r in data:
                if r[0] == "":
                    break
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
    dictarray["CORE"] = getList(core_list)
    dictarray["SME"] = getList(sme_list)
    dictarray["HSE"] = getList(hse_list)
    dictarray["PME"] = getList(pme_list)
    dictarray["GCE"] = getList(gce_list)
    # dictarray["CORE"] = getList(common_list)
    dictarray["Elective"] = getList(elective_list)
    dictarray["Humanities"] = getList(hrc_list)
    if common_list != []:
        dictarray["CORE"] = getList(common_list)
    
    # return dictarray
    array = {}
    for key, value in dictarray.items():
        if value:
            array[key] = value
    print(array)
    return array



# d = getData(4,"CE")
# for key, value in d.items():
#     if value:
#         print(key,"-")
#         for v in value:
#             print(v)
# print(d,"\n")

import externaldata
from externaldata import timetable



def getTimetable(codes, sem, branch):
    ref_array = getData(sem,branch)
    # print(ref_array)
    dictionary = {}
    newdic = {}
    data = ref_array.values()
    # print(data)
    # print("\n")
    for a in data:
        for b in a:
            code = b[0]
            details = b[1:]
            # print(code,":",details)
            dictionary[code] = details
    codelist = dictionary.keys()
    #print(codelist)
    for c in codes:
        if c in codelist:
            newdic[c] = dictionary[c]
    # return newdic

    # print("\n")
    t = timetable(newdic)
    print(t)
    outputdic = {}
    for key, value in t.items():
        temp = {}    
        temp['classes'] = []
        for v in value:
            [cN,cS] = v.split('.')
            temp2 = {}
            temp2['subject'] = cN
            temp2['time'] = cS
            temp['classes'].append(temp2)
        outputdic[key] = temp
    print(outputdic)
    return outputdic
    
# getData(4,"CE")
# getTimetable(['CE2020', 'CE2060', 'CE2040'],4,"CE")
# print(getData(4,"CE"))
# print(getTimetable(["CE2020","HS2302","CY3601","PH4602"],4,"CE"))
# print(getTimetable(["CS5016","CS5014","CS5616","PH3601","HS3605"],6,"CSE"))
'''{"PME": [["CS5016", "Computational Methods and Applications", "PA4+E4", 0], ["CS5014", "Foundations of Data Science and Machine Learning", "F", 0], ["CS5616", "Computational Complexity", "B", 0], ["CS5003", "Parameterized Algorithms", "H", 0], ["CS5633", "Model Checking", "C (Theory) + E2 (Lab)", 0], ["CS5639", "Topics in Networks", "PA2+\nE2", 0], ["CS5510", "Compiler Optimizations and Program Analysis", "L", 0], ["CS5638", "Quantum Computing ", "E\n(for registration)\n\n(contact instructors for further details on lecture timings)", 0], ["CS5010", "Graph Theory and Combinatorics", "I", 0], ["CS5002", "Functional Programming", "B", 0], ["DS5102", "Big Data Lab", "PM3", 0], ["DS3040", "Deep Learning ", "G and \nPM5 (tentative)", 0], ["DS6004", "Responsbile AI", "L", 0], ["EE5605", "Error-Correcting Codes for Communications and Distributed Systems", "F", 0], ["CS5642M", "Introduction To Machine Learning", "-", 0], ["CS5643M", "Reinforcement Learning ", "-", 0], ["CS5637M", "Secure Computation: Part I", "-", 0], ["CS4608M", "Cloud Computing", "-", 0], ["CS5XXX", "GPU Architectures and Programming", "-", 0]], "GCE": [["PH3601", "Quantum Mechanics for Engineers", "G", 0], ["PH4602", "Introduction to Special Relativity", "G", 0], ["HS4605", "Foundation of Linguistics (40)", "G", 0], ["HS5009", "Mental Health and Society in the Global South (40)", "G", 0], ["HS", "Contemporary Issues in Economic Development (30)", "G", 0], ["HS4607M", "German I (NPTEL)", "NA", 0], ["HS3605", "Introduction to Modern Indian Political Thought (NPTEL)", "NA", 0], ["ME3522", "Introduction to Finite Element Methods", "G", 0], ["CY3601", "Electrochemistry and Corrosions", "G", 0], ["ES 5601", "Sustainability Analysis and Design", "G", 0], ["BS5001", "Fundamentals of Nanobiotechnology", "G", 0], ["ES5XXXX", "Photosynthesis", "G", 0], ["EE5XXXX", "Computer Graphics (40)", "G", 0], ["ME5632", "Computational Methods for Inverse Problems", "G", 0], ["GN1005", "GN1005: How to prepare for internship and job search?", "E4", 0], ["CY4001", "Industrial Chemistry", "F", 0], ["HS3627", "Engineering Economics (40)*", "F", 0]]}'''