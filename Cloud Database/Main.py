import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def init_firestore():
    """
    Create a connection with the database
    """
    cred = credentials.Certificate("kennett-non-private-library-firebase-adminsdk-majer-bbfa3774ad.json")

    firebase_admin.initialize_app(cred, {
        "projectid" : "kennett-non-private-library"
    })

    cd = firestore.client()
    return cd

def addNewItem(cd):

    """
    Prompts user for input, and adds to database
    """
    name = input("Name of the book: ")
    pages = int(input("How many pages does it have: "))
    cat = True
    while cat == True:
        category = int(input("Fiction or Non-Fiction (0 - Fiction, 1 - Non-Fiction): "))
        if category == 1:
            category = "Non-Fiction"
            cat = False
        elif category == 0:
            category = "Fiction"
            cat = False
    qty = int(input("How many are in stock: "))

    result = cd.collection("inventory").document(name).get()

    if result.exists:
        print("ERROR, ITEM ALDREADY EXISTS.")
        return

    data = {
        "pages" : pages,
        "category" : category,
        "inStock" : qty
    }
    cd.collection("inventory").document(name).set(data)

def updateInventory(cd):
    name = input("Name: ")
    choice = int(input("(1) Add to inventory.\n(2)Subtract from inventory.\nYour Choice: "))
    qty = int(input("Quantity: "))

    result = cd.collection("inventory").document(name).get()

    if not result.exists:
        print("ERROR, ITEM DOES NOT EXIST. MAYBE YOU TYPED THE NAME WRONG? ")
        return

    data = result.to_dict()
    curqty = int(data["inStock"])
    if choice == 1:
        curqty += qty
    else:
        curqty -= qty

    data = {
        "pages" : data["pages"],
        "category" : data["category"],
        "inStock" : curqty
    }
    cd.collection("inventory").document(name).set(data)

def deleteInventory(cd):
    results = cd.collection("inventory").get()
    name = input("Name of item to delete: ")
    for result in results:
            if result.id == name:
                data = result.to_dict()
                inStock = data["inStock"]
                pages = data["pages"]
                category = data["category"]
                print(f"\n--{result.id}--\nSection:{category}\nPages: {pages}\nQuantity: {inStock}\n")
                choice = input("Are you sure you want to delete this item? (Y/N)")
                if choice.lower() == "y":
                    cd.collection("inventory").document(name).delete()
                    return
                print("Deletion cancelled. ")
                return
    print("ERROR, ITEM DOES NOT EXIST. MAYBE YOU TYPED THE NAME WRONG? ")
    return

def searchInventory(cd):
    results = cd.collection("inventory").get()
    print("How would you like to display results?" )
    choice = int(input("1. Display all\n2. Search by Name\n3. Search by category\nYour choice: "))

    if choice == 1:
        print("Displaying all:\n")
        for result in results:
            data = result.to_dict()
            inStock = data["inStock"]
            pages = data["pages"]
            category = data["category"]
            print(f"\n--{result.id}--\nSection:{category}\nPages: {pages}\nQuantity: {inStock}\n")

    elif choice == 2:
        name = input("Name: ")
        for result in results:
            if result.id == name:
                print("Found it! ")
                data = result.to_dict()
                inStock = data["inStock"]
                pages = data["pages"]
                category = data["category"]
                print(f"\n--{result.id}--\nSection:{category}\nPages: {pages}\nQuantity: {inStock}\n")
                return
            
        print("ERROR, ITEM DOES NOT EXIST. MAYBE YOU TYPED THE NAME WRONG? ")
        return
    
    elif choice == 3:
        categoryForSearch = input("Category: ")
        for result in results:
            data= result.to_dict()
            if data["category"] == categoryForSearch:
                inStock = data["inStock"]
                pages = data["pages"]
                category = data["category"]
                print(f"\n--{result.id}--\nSection:{category}\nPages: {pages}\nQuantity: {inStock}\n")
                

def main():
    cd = init_firestore()
    on = True
    while on == True:
        choice = int(input("Menu Options: \n1. Add new item\n2. Update Inventory Count\n3. Delete item from inventory\n4. Search Inventory\n0. End Program.\nYour Choice: "))
        if(choice == 0):
            on = False
        elif choice == 1:
            addNewItem(cd)
        elif choice == 2:
            updateInventory(cd)
        elif choice == 3:
            deleteInventory(cd)
        elif choice == 4:
            searchInventory(cd)

if __name__ == "__main__":
    main()