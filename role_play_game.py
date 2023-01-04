import sys
import random
 
points_player = points_ennemy = 50
 
player_atk = random.randint(5,10)
ennemy_atk = random.randint(5,15)
 
i = 0
while int(points_player) > 0 and int(points_ennemy) > 0:
    user_choice = input("Would you like to attack (1) or use a potion (2)? ")
 
    if int(user_choice) == 1: #case: attack (1)
        player_atk = random.randint(5,10)
        points_ennemy = int(points_ennemy) - int(player_atk)
 
        if points_ennemy > 0:
            print(f"""You inflicted {player_atk} damage to the enemy! 
            he now has {points_ennemy} points left """)
 
            ennemy_atk = random.randint(5,15)
            points_player = int(points_player) - int(ennemy_atk)
            if points_player > 0:
                print(f"""the enemy has inflicted on you {ennemy_atk} damage. 
                you have {points_player} left""")
 
            else:
                print(f"""the enemy has inflicted on you {ennemy_atk} damage.
                GAME OVER. """)
 
        else: 
            print(f"""You inflicted {player_atk} damage to the enemy!
            Congratulations! You have won the battle. """)
 
 
    elif int(user_choice) == 2: #case potion (2)
        while i<3:
         
            potion = random.randint(15,50)
            points_player = points_player + potion 
            i += 1
            print(f""""You've won {potion} points, your total LP are {points_player} ! 
            You have left {int("3") - int(i)} potions. """)
 
            ennemy_atk = random.randint(5,15)
            points_player = int(points_player) - int(ennemy_atk)
            print(f"""The enemy inflicted to you {ennemy_atk} damage 
            You have {points_player} left""")
            break
 
        else: #case 0 potion
            print("You have no potions left. ")
            continue
 
