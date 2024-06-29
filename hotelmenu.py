#project using dictionary datatype and conditional statement.

 #define the menu of restaurant

menu = {
    'Pizza': 99,
    'Pasta': 70,
    'Burgur': 60,
    'Coffee': 30,
    'Tea': 20,
    'Momos': 40,
    'Chocolate Shake': 120,
}
#Geed
print("WELCOME TO TEN ELEVEN RESTAURANT")
print("Pizza: Rs99\nPasta: Rs70\nBurgur: Rs60\nCoffee: Rs30\nTea: Rs20\nMomos: Rs40\nChocolate Shake: Rs120")

order_total = 0
#60 + 70 =130

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0+ 50
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not avaialable yet!")

    another_order = input("Do you want to add another item? (Yes/No)")
    if another_order == "Yes":
        item_2 = input("Enter the name of second item =")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"item {item_2} has been added to oder")
        else:
            print(f"ordered item {item_2} is not avaialable!")

print(f"The total amount of items to pay {order_total}")









