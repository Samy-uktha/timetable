import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from function import getData
from function import getTimetable
import csv
import json
from typing import List
app = FastAPI()

class DataInput(BaseModel):
    semester:str
    branch:str

class DataInput2(BaseModel):
    semester:str
    branch:str
    selectedCourses:List[str]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def index():
    print("Hi")
    print("yooooo")
    # getTimetable(["CS5016","CS5014","CS5616","PH3601","HS3605"],6,"CSE")
    getTimetable(['CE2020', 'CE2060', 'CE2040'],4,"CE")
    # gettable("CSE")Time
    return {"message": "Welcome to the API 2"}

@app.post("/courses")
async def getCourses(input_data: DataInput):
    
    sem = int(input_data.semester[0])
    branch = input_data.branch
    print(sem  , branch)
    courses = getData(sem, branch)
    courses = dict(courses)
    print(courses)
    r = json.dumps(courses)
    return {"result" : r}
@app.post("/courselist")
async def getTimetable2(input_data: DataInput2):
    sem = int(input_data.semester[0])
    branch = input_data.branch
    selected_courses = input_data.selectedCourses
    print(sem, branch, selected_courses)
    courselist = getTimetable(selected_courses, sem, branch)
    print(courselist)
    return {"result" : courselist}



if __name__ == "__main__":
    
    uvicorn.run(app, port=8000, host="127.0.0.1")
    

# {"CORE": [["CE2020", "Structural Analysis", "A", "PA1"], ["CE2060", "Soil Mechanics", "B", "PA3"], ["CE2040", "Hydraulic Engineering", "C", "PA5"]], "SME": [["MA2041", "Probability and Statistics", "F", 0], ["MA2032", "Numerical Analysis", "F", 0], ["PH4602", "Introduction to Special Relativity", "G", 0], ["PH3601", "Quantum Mechanics for Engineers", "G", 0], ["CY3601", "Electrochemistry and Corrosions", "G", 0], ["CY4001", "Industrial Chemistry", "F", 0]], "HSE": [["HS2031", "Principles of Economics (40)", "H", 0], ["HS2302", "Introduction to Language and Society(40)", "H", 0], ["HSxxxx", "Mental Health and Law (tentative title , course yet to be approved) (40)", "H", 0], ["HS2304", "Culture and Gender Performativity(40) ", "H", 0]], "GCE": [["PH3601", "Quantum Mechanics for Engineers", "G", 0], ["PH4602", "Introduction to Special Relativity", "G", 0], ["HS4605", "Foundation of Linguistics (40)", "G", 0], ["HS5009", "Mental Health and Society in the Global South (40)", "G", 0], ["HS", "Contemporary Issues in Economic Development (30)", "G", 0], ["HS4607M", "German I (NPTEL)", "NA", 0], ["HS3605", "Introduction to Modern Indian Political Thought (NPTEL)", "NA", 0], ["ME3522", "Introduction to Finite Element Methods", "G", 0], ["CY3601", "Electrochemistry and Corrosions", "G", 0], ["ES 5601", "Sustainability Analysis and Design", "G", 0], ["BS5001", "Fundamentals of Nanobiotechnology", "G", 0], ["ES5XXXX", "Photosynthesis", "G", 0], ["EE5XXXX", "Computer Graphics (40)", "G", 0], ["ME5632", "Computational Methods for Inverse Problems", "G", 0], ["GN1005", "GN1005: How to prepare for internship and job search?", "E4", 0], ["CY4001", "Industrial Chemistry", "F", 0], ["HS3627", "Engineering Economics (40)*", "F", 0]]}
