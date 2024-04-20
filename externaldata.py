import csv
import json
import re
# csv_array = ["timetable\srujana files\btech_sem2.csv",
#              "timetable\srujana files\btech_sem2_sem4_civil.csv",#timetable\srujana files\btech_sem2_ds.csv
#              "timetable\srujana files\btech_sem2_sem4_cse.csv",
#              "timetable\srujana files\btech_sem2_sem4_hse.csv",
#              "timetable\srujana files\btech_sem2_sem4_sme.csv",
#              "timetable\srujana files\btech_sem6_civil.csv",
#              "timetable\srujana files\btech_sem6_cse.csv",
#              "timetable\srujana files\btech_sem8_civil.csv",
#              "timetable\srujana files\btech_sem8_cse.csv",
#              "timetable\srujana files\civil_pme.csv",
#              "timetable\srujana files\cse_pme.csv",
#              "timetable\srujana files\GCE.csv",#timetable\srujana files\cse_pme.csv
#              "timetable\srujana files\btech_sem2_ds.csv",
#              "timetable\srujana files\btech_sem2_sem4_ee.csv",
#              "timetable\srujana files\btech_sem2_sem4_me.csv",
#              "timetable\srujana files\btech_sem6_ee.csv",
#              "timetable\srujana files\btech_sem6_me.csv",
#              "timetable\srujana files\btech_sem8_ee.csv",
#              "timetable\srujana files\btech_sem8_me.csv",
#              "timetable\srujana files\ee_pme.csv",
#              "timetable\srujana files\me_pme.csv"]
# def course(degree,sem,branch):
#     course_list = []
#     for i in csv_array:
#         if degree.lower() in i and str(sem).lower() in i and branch.lower() in i:
#             course_list.append(i)
#     if degree.lower() == 'btech' and (sem == 6 or sem==8):
#         course_list.append(f"timetable\srujana files\{branch}_pme.csv")
#         course_list.append("timetable\srujana files\GCE.csv")
#     courses = []
#     for k in course_list:
#         #print(k)
#         l = []
#         with open(k,newline='') as file:
#             csvFile = csv.reader(file)
#             for lines in csvFile:
#                 l.append(lines)
#         #print(l)
#         m=0
#         for i in range(len(l)):
#             for j in range(len(l[i])):
#                 if l[i][j] == 'Slot':
#                     m=j

#         for i in range(4,len(l)):
#             if l[i][0].startswith("EE") or l[i][0].startswith("CS") or l[i][0].startswith("ME")  or l[i][0].startswith("CE") or l[i][0].startswith("HS") or l[i][0].startswith("MA") or l[i][0].startswith("CY") or l[i][0].startswith("DS"):
#                 matches = re.findall(r'\b(?:A|B|C|D|PA1|PA2|PA3|PA4|H|PM1|I|J|E1|M2|F|G|PM2|M3|K|L|E2|Q|R|M4|EML|M5|PA5|PM5|E)\b',l[i][m])
#                 if l[i][0].endswith('M') or ('XXX' in l[i][0] and 'XXXX' not in l[i][0]):
#                     matches = ['NPTEL']
#                 dct = {
#                     l[i][0] : [l[i][1],matches]
#                 }
#                 courses.append(dct)
#     return course_list,courses
    
# cl,c = course('btech',6,'cse')
# print(c)
# for i in c:
#    print(i)
#    print()
# day_slot = {
#         "Monday" : ['A','B','C','H','PM1','I','J','PA1','E1'],
#         "Tuesday" : ['M2','F','G','D','PM2','K','L','E2','PA2'],
#         "Wednesday" : ['M3','A','B','C','H','PM3','Q','R','PA3','EML'],
#         "Thursday" : ['M4','F','G','D','PM4','K','L','PA4','E4'],
#         "Friday" : ['M5','A','B','C','H','I','J','E5','PM5','PA5'],
#         "NPTEL" : "nptel course"
#     }
# slot_timings = {
# "A"	:"9:00 - 9:50",
# "B" :	"10:00-10:50",
# "C"	: "11:00-11:50",
# "D" :	"12:00-12:50",
# "E1":	"17:10-18:00",
# "E2"	:"17:10-18:00",
# "E4":	"17:10-18:00",
# "E5":	"17:10-18:00",
# "F":	"9:00 - 10:15",
# "G"	:"10:30-11:45",
# "H":	"12:05-12:55",
# "I":	"14:00-15:15",
# "J":	"15:30-16:45",
# "K":	"14:00-15:15",
# "L"	:"15:30-16:45",
# "PM1":	"10:00-12:55",
# "PM2"	:"9:00-11:45",
# "PM3":	"10:00-12:55",
# "PM4":	"9:00-11:45",
# "PM5":	"10:00-12:55",
# "Q"	:"14:00-14:50",
# "R":	"15:00-15:50",
# "EML"	:"16:00-18:00",
# "PA1":	"14:00-16:45",
# "PA2":	"14:00-16:45",
# "PA3"	:"14:00-15:50",
# "PA4"	:"14:00-16:45",
# "PA5"	:"14:00-16:45",
# "M1"	:"8:00 - 8:50",
# "M2"	:"8:00 - 8:50",
# "M3"	:"8:00 - 8:50",
# "M4"	:"8:00 - 8:50",
# "M5":	"8:00 - 8:50"
# }

# def timetable(c):
    
#     day_slot = {
#         "Monday" : ['A','B','C','H','PM1','I','J','PA1','E1'],
#         "Tuesday" : ['M2','F','G','D','PM2','K','L','E2','PA2'],
#         "Wednesday" : ['M3','A','B','C','H','PM3','Q','R','PA3','EML'],
#         "Thursday" : ['M4','F','G','D','PM4','K','L','PA4','E4'],
#         "Friday" : ['M5','A','B','C','H','I','J','E5','PM5','PA5'],
#         "NPTEL" : "nptel course"
#     }
#     slot_timings = {
#     "A"	:"9:00 - 9:50",
#     "B" :	"10:00-10:50",
#     "C"	: "11:00-11:50",
#     "D" :	"12:00-12:50",
#     "E1":	"17:10-18:00",
#     "E2"	:"17:10-18:00",
#     "E4":	"17:10-18:00",
#     "E5":	"17:10-18:00",
#     "F":	"9:00 - 10:15",
#     "G"	:"10:30-11:45",
#     "H":	"12:05-12:55",
#     "I":	"14:00-15:15",
#     "J":	"15:30-16:45",
#     "K":	"14:00-15:15",
#     "L"	:"15:30-16:45",
#     "PM1":	"10:00-12:55",
#     "PM2"	:"9:00-11:45",
#     "PM3":	"10:00-12:55",
#     "PM4":	"9:00-11:45",
#     "PM5":	"10:00-12:55",
#     "Q"	:"14:00-14:50",
#     "R":	"15:00-15:50",
#     "EML"	:"16:00-18:00",
#     "PA1":	"14:00-16:45",
#     "PA2":	"14:00-16:45",
#     "PA3"	:"14:00-15:50",
#     "PA4"	:"14:00-16:45",
#     "PA5"	:"14:00-16:45",
#     "M1"	:"8:00 - 8:50",
#     "M2"	:"8:00 - 8:50",
#     "M3"	:"8:00 - 8:50",
#     "M4"	:"8:00 - 8:50",
#     "M5":	"8:00 - 8:50"
#     }


#     ls = []
#     rs={
#     "Monday" : [],
#     "Tuesday" : [],
#     "Wednesday" : [],
#     "Thursday" : [],
#     "Friday" : [],
#     "NPTEL" :[]
# }
#     for n in c:
#         for key,value in n.items():
#             ls.append(value)
#     for i in ls:
#         for k in range(len(i[1])):
#                     if i[1][k] in day_slot["Monday"]:
#                         rs["Monday"].append(i[0]+" - "+slot_timings[i[1][k]])
#                     if i[1][k] in day_slot["Tuesday"]:
#                         rs["Tuesday"].append(i[0]+" - "+slot_timings[i[1][k]])
#                     if i[1][k] in day_slot["Wednesday"]:
#                         rs["Wednesday"].append(i[0]+" - "+slot_timings[i[1][k]])
#                     if i[1][k] in day_slot["Thursday"]:
#                         rs["Thursday"].append(i[0]+" - "+slot_timings[i[1][k]])
#                     if i[1][k] in day_slot["Friday"]:
#                         rs["Friday"].append(i[0]+" - "+slot_timings[i[1][k]])
#                     if i[1][k] == "NPTEL":
#                         rs["NPTEL"].append(i[0])
#     for key,value in rs.items():
#         print(key,":")
#         for val in value:
#             print(" ",val)
#         print()


def timetable(c):

    day_slot = {
        "Monday" : ['A','B','C','H','PM1','I','J','PA1','E1'],
        "Tuesday" : ['M2','F','G','D','PM2','K','L','E2','PA2'],
        "Wednesday" : ['M3','A','B','C','H','PM3','Q','R','PA3','EML'],
        "Thursday" : ['M4','F','G','D','PM4','K','L','PA4','E4'],
        "Friday" : ['M5','A','B','C','H','I','J','E5','PM5','PA5'],
        "NPTEL" : "nptel course"
    }
    slot_timings = {
    "A"	:"9:00-9:50",
    "B" :	"10:00-10:50",
    "C"	: "11:00-11:50",
    "D" :	"12:00-12:50",
    "E1":	"17:10-18:00",
    "E2"	:"17:10-18:00",
    "E4":	"17:10-18:00",
    "E5":	"17:10-18:00",
    "F":	"9:00-10:15",
    "G"	:"10:30-11:45",
    "H":	"12:05-12:55",
    "I":	"14:00-15:15",
    "J":	"15:30-16:45",
    "K":	"14:00-15:15",
    "L"	:"15:30-16:45",
    "PM1":	"10:00-12:55",
    "PM2"	:"9:00-11:45",
    "PM3":	"10:00-12:55",
    "PM4":	"9:00-11:45",
    "PM5":	"10:00-12:55",
    "Q"	:"14:00-14:50",
    "R":	"15:00-15:50",
    "EML"	:"16:00-18:00",
    "PA1":	"14:00-16:45",
    "PA2":	"14:00-16:45",
    "PA3"	:"14:00-15:50",
    "PA4"	:"14:00-16:45",
    "PA5"	:"14:00-16:45",
    "M1"	:"8:00-8:50",
    "M2"	:"8:00-8:50",
    "M3"	:"8:00-8:50",
    "M4"	:"8:00-8:50",
    "M5":	"8:00-8:50"
    }


    ls = []
    rs={
    "Monday" : [],
    "Tuesday" : [],
    "Wednesday" : [],
    "Thursday" : [],
    "Friday" : [],
    "NPTEL" :[]
    }
    for key,value in c.items():
        ls.append(value)
    # print(ls)
    for i in ls:
        for k in range(1,len(i)):
                    if i[k] in day_slot["Monday"]:
                        rs["Monday"].append(i[0]+"."+slot_timings[i[k]])
                    if i[k] in day_slot["Tuesday"]:
                        rs["Tuesday"].append(i[0]+"."+slot_timings[i[k]])
                    if i[k] in day_slot["Wednesday"]:
                        rs["Wednesday"].append(i[0]+"."+slot_timings[i[k]])
                    if i[k] in day_slot["Thursday"]:
                        rs["Thursday"].append(i[0]+"."+slot_timings[i[k]])
                    if i[k] in day_slot["Friday"]:
                        rs["Friday"].append(i[0]+"."+slot_timings[i[k]])
                    if i[k] == "NPTEL":
                        rs["NPTEL"].append(i[0])
    # for key,value in rs.items():
    #     print(key,":")
    #     for val in value:
    #         print(" ",val)
    #     print()
    return rs
    



    
# timetable(c)

# d = course('btech',6,'cse')
# timetable(d)