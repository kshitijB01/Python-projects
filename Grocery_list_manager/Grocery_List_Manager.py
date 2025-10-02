#Grocery list manager

Grocery_List = ["Potatoes", "Onions", "Tomatoes", "Green chillies", "Garlic", "Ginger","Spinach", "Coriander", "Cauliflower", "Cabbage", "Ladyfinger", "Bottle gourd", "Brinjal", "Seasonal vegetables", "Bananas", "Apples (when in budget)", "Oranges / Sweet lime",
        "Papaya", "Watermelon (seasonal)", "Mango (seasonal)","Rice (regular)", "Wheat flour (Atta)", "Poha", "Suji / Rava", "Oats (optional)", "Toor dal (Arhar dal)", "Chana dal", "Moong dal", "Masoor dal",
        "Kabuli chana (Chickpeas)", "Rajma (Kidney beans)", "Green gram (Moong whole)",  "Salt", "Turmeric powder", "Red chilli powder", "Coriander powder",
        "Cumin seeds", "Mustard seeds", "Garam masala", "Hing (Asafoetida)","Cooking oil (Sunflower / Mustard / Soybean)", "Ghee (small pack)",
        "Milk", "Curd (or homemade)", "Paneer (occasionally)","Bread", "Butter (small pack)", "Biscuits (Parle-G, Marie, etc.)","Tea leaves / Coffee", "Sugar / Jaggery", "Noodles (Maggi type)","Namkeen (Haldiram/Local)","Bathing Soap", "Shampoo (economical pack)", "Toothpaste",
        "Detergent", "Dishwashing bar/liquid", "Floor cleaner"]

task = input("Enter the task(add, remove, search, view) you want to perform: ")

if task == "add":
    n = int(input("Enter how many items you want to add: "))

    for i in range(n):
        item = input(f"Enter items {i+1}: ")
        Grocery_List.append(item) 

    print(Grocery_List)

elif task == "remove":
    n = int(input("Enter how many items you want to remove: "))

    for i in range(n):
        item = input(f"Enter items {i+1}: ")
        if item in Grocery_List:
            Grocery_List.remove(item)

            print(Grocery_List)
        else:
            print(f"{item} not found in list.")

    

elif task == "search":
    n = int(input("Enter how many items you want to search: "))

    for i in range(n):
        item = input(f"Enter items {i+1}: ")
        if item in Grocery_List:
            print("Yes the entered item is present in list")
        else:
            print("No the entered item is not present in list")

elif task == "view":
    print(Grocery_List)

else:
    print(Grocery_List)


