import sys
import random
 
nombre_mystere = random.randint(0,100)
print(nombre_mystere)
 
i = 0
#main loop
while i < 5:
 
    nombre_donne = input("Please enter a number between 1 and 100 ")
  
    #case user gets the correct number
    if  ( nombre_donne.isdigit() == True ) and (int(nombre_donne) >= 0) and (int(nombre_donne) <= 100):
        if int(nombre_donne) == int(nombre_mystere):
            i += 1
            print(f"Congratulations, you have found the mysterious number in {i} trials! ")
            sys.exit()
            
        #case the number is bigger
        elif int(nombre_donne) < int(nombre_mystere):
            i += 1
            print(f"""The mysterious number is bigger than {nombre_donne}
            Il vous reste {int(5) - (i)} essais""")
            
        #case the number is smaller
        elif int(nombre_donne) > int(nombre_mystere):
            i += 1
            print(f"""The mysterious number is smaller than {nombre_donne}
            Il vous reste {int(5) - (i)} essais""")
            
    #case invalid value
    else:
        print("Please enter a valid value ")
        
    #case no trials
else: 
            print("You have no trials left ")
            sys.exit()
 
