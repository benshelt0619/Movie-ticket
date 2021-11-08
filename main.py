r_age=17 #sets the minimum age
user_age=input("Age? ") #Asking for user's age
user_age=int(user_age) #Convert string to an integer
if user_age >= r_age: #If age is 17 or larger, they can buy a ticket
  print("You're old enough ") #Print this
else: #If not 17, buy a PG-13 ticket
   print("Buy a PG-13 ticket you baby ") #Print this
