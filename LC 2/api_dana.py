# Libraries
from fastapi import FastAPI, HTTPException

import uvicorn

# Bikin instance untuk menangkap REST API (fast API)
dana = FastAPI()

# Enpoint utama
@dana.get("/")
def home():
    return {"message":"Anjing Lu! Tai",
            "menu":{1:"students",
                    2:"players",
                    3:"/shopping_cart"}}

############ Load from json ###########
students = {
    "Joni":{
        "shoe_size":44,
        "fav_color":"Black"
    },
    "Salsa":{
        "shoe_size":39,
        "fav_color":"White"
    },
    "Dewa":{
        "shoe_size":42,
        "fav_color":"Blue"
    }
}

# Endpoint students
@dana.get("/students")
def students():
    return {"message":"ini merupakan api untuk menampilakn mengubah nemabmbah mengedit dan menghapus"
            "menu":{
                 1:"/students_data",
                 2:"/find_students/{name}",
                 3:"/add_students",
                 4:"/update_student/{name}",
                 5:"/delete_student/{name}"
            }}

# Endpoint menampilkan semua data
@dana.get("/students/data")
def std_data():
    return students

@dana.get("/students/find_student/{name}")
def find_student (name:str):

    if name in students_data.keys()
# Endpoint menambah data siswa 
@dana.post("/students/add_students")
def add_std(student_data:dict):
    #menangkap pesan print dalam terminal
    print (f"student Data: {student_data}")
    #Menangkap masukan user
    student_name = student_data["name"]
    student_shoe_size = student_data["shoe_size"]
    student_fav_color = student_data["fav_color"]
    #untuk menambahkan data ke dalam dictionary
    students_data[student_name] = {
        "shoe_size":student_shoe_size,
        "fav_color":student_fav_color
    }
    #Untuk Menambahkan pesan dalam tampilan api 
    return {"message":f"student{student_name} sucessfully added!"}

#Endpoint untuk update/edit data 
@dana.put("/students/update_student/{name}")
def put_std(name:str, student_data:dict)
    #Conditional pengecekan apakah nama ada dalam data 
    if name not in students_data.keys():
        raise HTTPException (status_code=404, detail=f"student {name} not found!")
    else:
        #Assign variables
        students_data[name] = student_data
        #menampilkan pesan dalam API
        return {"message":f"students data {name} has been updated}