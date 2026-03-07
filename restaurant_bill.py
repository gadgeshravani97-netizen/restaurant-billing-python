#restuarant menu
print("Welcome to our restruarant\n")
print("here is our menu")

food_menu={
    "pizza":200,
    "noodels":100,
    "burger":150,
    "panipuri":50,
}
drink_menu={
      "juice of mixer of seven fruit":100,
      "coffee":90,
      "coka cola 500ml":150,
      "cooled water":40,
}

total=0

print(food_menu,"\n")
item1=str(input("enter your first order:"))
if(item1 in food_menu):
   total+= food_menu[item1]
   print("your order is conformed that is",item1)
else:
   print("we don't produce that")

item2=input("would youlike to order further? yes/no\n:").lower()
if item2=="yes":
   item3 = input("enter your second order:").lower()

   if(item3 in food_menu):
      print("your order is conformed that is",item3)
      total+=food_menu[item3]
   else:
      print("we don't produce that\n")
else:
   print("order is placed.\n")

item4=str(input("what order drinks further? yes/no\n:")) 
if item4== "yes":
   print(drink_menu)
   item5=input(("what would you like to drinkforn the menu:")).lower()

   if item5 in drink_menu:
      total+=drink_menu[item5]
      print("your whole order is placed") 

   else:
      print("We do not produse that\n")

print("your total bill is:",total)





