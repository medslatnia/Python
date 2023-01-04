import sys
 
liste_course = []
 
menu = """Choose one of the 5 options:
1: Add an element to the list
2: Delete an element from the list
3: Display the list
4: Clear the list
5: Exit
Your choice is: """
 
menu_choices = ["1", "2", "3", "4", "5"]
 
while True:
 
    user_choice = input(menu)
 
#case invalid value
    if user_choice not in menu_choices: 
        print("Please enter a valid value ")
        continue
 
#case add element
    elif user_choice == "1": 
        element = input("Enter the element's name: ")
        liste_course.append(element)
        print(f"{element} has been added to the list")
 
#case delete element
    elif user_choice == "2": 
        element = input("Please enter the element to delete: ")
        if element in liste_course:
            liste_course.remove(element)
            print(f"{element} has been deleted. ")
        else:
            print("This element doesn't exist in the list. ")
 
#case display list
    elif user_choice == "3": 
        print(liste_course)
 
#case clear list
    elif user_choice == "4": 
        liste_course.clear()
        print("The list has been cleared. ")
 
#case exit 
    elif user_choice == "5":
        print("Thank you, goodbye! ")
        sys.exit()
