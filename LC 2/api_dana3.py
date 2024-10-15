from fastapi import FastAPI, HTTPException, Header
import uvicorn
import pandas as pd

# Bikin instance untuk menangkap REST API (Fast API)
dana = FastAPI()

# --reload = while True, akan terus dijalankan

# Endpoint Utama (API cuma bisa baca dictionary)
@dana.get("/") # Setara dengan 127:0.0.1:8000/ atau localhost:8000/
def home():
    return {"message": "Hello World! This is my first API",
            "menu":{1:"/students",
                     2:"/players",
                     3:"/shopping_cart"}}



####################Load From JSON####################
students_data = {
    "Joni":{
        "shoe_size":44,
        "fav_color":"Black"
    },
    "Salsa":{
        "shoe_size":39,
        "fav_color":"White"
    },
    "Dewa":{
        "show_size":42,
        "fav_color":"Green"
    }

}

# Endpoint Students
@dana.get("/students")
def students():
    return {"message":"Ini merupakan API untuk menampilkan, menambah, mengedit, dan menghapus data siswa",
            "menu":{
                1:"/data",
                2:"/find_students/{name}",
                3:"/add_students",
                4:"/update_student/{name}",
                5:"/delete_students/{name}"
            }}

# Endpoint menampilkan semua data
@dana.get("/students/data")
def std_data():
    return students_data

# Endpoint menambah data siswa
@dana.post("/students/add_student")
def add_std(student_data:dict):
    # Untuk menambahkan print pesan dalam terminal
    print(f"Student Data {student_data}")
    # Untuk menambahkan data dalam dictionary
    student_name = student_data["name"]
    student_shoe_size = student_data["shoe_size"]
    student_fav_color = student_data["fav_color"]
    student_data[student_name] = {
        "shoe_size":student_shoe_size,
        "fav_color":student_fav_color
    }

    # Menambahkan pesan dalam tampilan API
    return {"message":f"Student {student_name} succesfully added!"}

####################Load From CSV#####################



@dana.get("/students/find_student/{name}")
def find_student(name:str):
    # Kondisional/Pengecekan Apakah nama siswa ada dalam data?
    if name in students_data.keys():
        return {name:students_data[name]}
    else:
        raise HTTPException(status_code=404, detail="Student Not Found!")
    
@dana.delete("/students/delete_student/{name}")
def del_std(name:str):
    if name in students_data.keys():
        #hapus data siswa berdasarkan asil slicing dictionary
        del students_data[name]
        return {"message":f"student data{name} has been deleted!"}
    else:
        raise HTTPException(status_code=404 , detail=f"student {name} not found")


# HTTP hanya untuk method GET saja
# Swagger UI untuk dapat digunakan untuk selain GET

######################################################
####################Load From CSV#####################


df = pd.read_csv("C:\Program Files\Hacktiv8\Phase 0\LC 2\horse_clean.csv")

horse = pd.read_csv("C:\Program Files\Hacktiv8\Phase 0\LC 2\horse_clean.csv")

#endpoint horse home
@dana.get("/horses")
def kandang():
    return {"message":"selamat datang di sub menu perkudaan",
            "menu":{
                1:"get all horses (horses/data)",
                2:"filter by surgery(/horses/surgery/{surg})",
                3:"filter by age(/horses/surgery/{age})",
                4:"filter by outcome(/horses/surgery/{out})",
                5:"Delete One of horse data by unnamed *Sad:'( (/horses/del/{outcome})"
                
            }}

# Endpoint show horses data 
@dana.get("/horses/data")
def kuda():
    return horse.to_dict(orient="records")

# Endpoint Filter Surgery
@dana.get("/horses/surgery/{surgery_type}")
def operasi(surgery_type:str):
    #menyimpan sloicng dalam variabel baru 
    horse_surgery = horse[horse["surgery"]==surgery_type]
    #return hasil slicing
    return horse_surgery.to_dict(orient="records")

# Endpoint Filter age
@dana.get("/horses/age/{age_type}")
def umur(age_type:str):
    #menyimpan sloicng dalam variabel baru 
    horse_age = horse[horse["age"]==age_type]
    #return hasil slicing
    return horse_age.to_dict(orient="records")


@dana.get("/horses/outcome/{outcome_type}")
def outcome(outcome_type:str):
    #menyimpan sloicng dalam variabel baru 
    horse.outcome = horse[horse["outcome"]==outcome_type]
    #return hasil slicing
    return horse.outcome.to_dict(orient="records")

#API KEY (PASSWORD)
API_KEY = "admin1234"

##################
@dana.delete("/horses/del/{id}")
def apus(id:int, api_key:str=Header(None)): #Memasang API Key dalam header dengan default Value None
    #Pengencekan Api KEY
    if api_key is None or api_key !=API_KEY:
        raise HTTPException(status_code=401, detail="api key masing kosong atau salah")
    #Kalo API Key bener 
    else:
        #pengecekan apakah ada ada dalam kolom unnamed: 0 
        if id not in horse ["Unnamed: 0"]: 
            raise HTTPException(status_code=404 , details=f"Horse with id {id} did not found!")
        #Kalo ketemu/adda 
        else: horse.drop(horse[horse["Unnamed: 0"]==id].index, inplace=True)
        return{"message":f"Horse data with id {id} Successfuly deleted!"}

######################################################
#Shopping Cart
######################################################

cart = {"name": "shopping cart",
        "columns": ["prod_name", "price", "num_items"],
        "items": {}}


@dana.get("/shopping_cart")
def root():
    return {"message": "Welcome to Toko H8 Shopping Cart! There are some features that you can explore",
            "menu": {1: "See shopping cart (/shopping_cart/cart)",
                     2: "Add item (/shopping_cart/add)",
                     3: "Edit shopping cart (/shopping_cart/edit/{id})",
                     4: "Delete item from shopping cart (/shopping_cart/del/{id})",
                     5: "Calculate total price (/shopping_cart/total)",
                     6: "Exit (/shopping_cart/exit)"}
            }

@dana.get("/shopping_cart/cart")
def show():
    return cart


@dana.post("/shopping_cart/add")
def add_item(added_item: dict):
    id = len(cart["items"].keys()) + 1
    cart["items"][id] = added_item
    return f"Item successfully added into your cart with ID {id}"


@dana.put("/shopping_cart/edit/{id}")
def update_cart(id: int, updated_cart: dict):
    if id not in cart['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        cart["items"][id].update(updated_cart)
        return {"message": f"Item with ID {id} has been updated successfully."}


@dana.delete("/shopping_cart/del/{id}")
def remove_row(id: int):
    if id not in cart['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        cart["items"].pop(id)
        return {"message": f"Item with ID {id} has been deleted successfully."}


@dana.get("/shopping_cart/total")
def get_total():
    total_price = sum(item["price"] * item["num_items"] for item in cart["items"].values())
    return {"total_price": total_price}


@dana.get("/shopping_cart/exit")
def exit():
    return {"message": "Thank you for using Toko H8 Shopping Cart! See you next time."}

if __name__ =="__main__":
    uvicorn.run("api_dana3:dana", host="127.0.0.1", port=8000, reload=True )