from fastapi import FastAPI, HTTPException, Header
import uvicorn
import pandas as pd

# Create an instance for FastAPI
dana = FastAPI()

# Main endpoint
@dana.get("/")
def home():
    return {
        "message": "Hello World! This is my first API",
        "menu": {
            1: "/students",
            2: "/players",
            3: "/shopping_cart"
        }
    }

#################### Load From JSON ####################
students_data = {
    "Joni": {
        "shoe_size": 44,
        "fav_color": "Black"
    },
    "Salsa": {
        "shoe_size": 39,
        "fav_color": "White"
    },
    "Dewa": {
        "shoe_size": 42,
        "fav_color": "Green"
    }
}

# Students endpoint
@dana.get("/students")
def students():
    return {
        "message": "Ini merupakan API untuk menampilkan, menambah, mengedit, dan menghapus data siswa",
        "menu": {
            1: "/data",
            2: "/find_students/{name}",
            3: "/add_students",
            4: "/update_student/{name}",
            5: "/delete_students/{name}"
        }
    }

# Endpoint to show all student data
@dana.get("/students/data")
def std_data():
    return students_data

# Endpoint to add student data
@dana.post("/students/add_student")
def add_std(student_data: dict):
    student_name = student_data["name"]
    students_data[student_name] = {
        "shoe_size": student_data["shoe_size"],
        "fav_color": student_data["fav_color"]
    }
    return {"message": f"Student {student_name} successfully added!"}

# Find student by name
@dana.get("/students/find_student/{name}")
def find_student(name: str):
    if name in students_data.keys():
        return {name: students_data[name]}
    else:
        raise HTTPException(status_code=404, detail="Student Not Found!")

# Delete student by name
@dana.delete("/students/delete_student/{name}")
def del_std(name: str):
    if name in students_data.keys():
        del students_data[name]
        return {"message": f"Student {name} has been deleted!"}
    else:
        raise HTTPException(status_code=404, detail=f"Student {name} not found")


#################### Load From CSV ####################
# Load the CSV data
df = pd.read_csv(r"C:\Program Files\Hacktiv8\Phase 0\LC 2\horse_clean.csv")
horse = pd.read_csv(r"C:\Program Files\Hacktiv8\Phase 0\LC 2\horse_clean.csv")

# Horses endpoint
@dana.get("/horses")
def kandang():
    return {
        "message": "Selamat datang di sub menu perkudaan",
        "menu": {
            1: "Get all horses (horses/data)",
            2: "Filter by surgery (/horses/surgery/{surg})",
            3: "Filter by age (/horses/age/{age})",
            4: "Filter by outcome (/horses/outcome/{out})",
            5: "Delete one horse by ID (/horses/del/{id})"
        }
    }

# Show all horses data
@dana.get("/horses/data")
def kuda():
    return horse.to_dict(orient="records")

# Filter horses by surgery
@dana.get("/horses/surgery/{surgery_type}")
def operasi(surgery_type: str):
    horse_surgery = horse[horse["surgery"] == surgery_type]
    return horse_surgery.to_dict(orient="records")

# Filter horses by age
@dana.get("/horses/age/{age_type}")
def umur(age_type: str):
    horse_age = horse[horse["age"] == age_type]
    return horse_age.to_dict(orient="records")

# Filter horses by outcome
@dana.get("/horses/outcome/{outcome_type}")
def outcome(outcome_type: str):
    horse_outcome = horse[horse["outcome"] == outcome_type]
    return horse_outcome.to_dict(orient="records")

# Delete horse data by ID with API key authentication
API_KEY = "admin1234"

@dana.delete("/horses/del/{id}")
def apus(id: int, api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API key is missing or incorrect")
    else:
        if id not in horse["Unnamed: 0"].values:
            raise HTTPException(status_code=404, detail=f"Horse with id {id} not found!")
        else:
            horse.drop(horse[horse["Unnamed: 0"] == id].index, inplace=True)
            return {"message": f"Horse data with id {id} successfully deleted!"}


######################################################
# Shopping Cart
######################################################

cart = {"name": "shopping cart",
        "columns": ["prod_name", "price", "num_items"],
        "items": {}}

# Shopping cart main menu
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

# Show shopping cart items
@dana.get("/shopping_cart/cart")
def show():
    return cart

# Add item to shopping cart
@dana.post("/shopping_cart/add")
def add_item(added_item: dict):
    id = len(cart["items"].keys()) + 1
    cart["items"][id] = added_item
    return f"Item successfully added into your cart with ID {id}"

# Edit shopping cart item
@dana.put("/shopping_cart/edit/{id}")
def update_cart(id: int, updated_cart: dict):
    if id not in cart['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        cart["items"][id].update(updated_cart)
        return {"message": f"Item with ID {id} has been updated successfully."}

# Delete item from shopping cart
@dana.delete("/shopping_cart/del/{id}")
def remove_row(id: int):
    if id not in cart['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        cart["items"].pop(id)
        return {"message": f"Item with ID {id} has been deleted successfully."}

# Calculate total price of shopping cart
@dana.get("/shopping_cart/total")
def get_total():
    total_price = sum(item["price"] * item["num_items"] for item in cart["items"].values())
    return {"total_price": total_price}

# Exit shopping cart
@dana.get("/shopping_cart/exit")
def exit():
    return {"message": "Thank you for using Toko H8 Shopping Cart! See you next time."}

if __name__ == "__main__":
    uvicorn.run("api_dana3:dana", host="127.0.0.1", port=8000, reload=True)