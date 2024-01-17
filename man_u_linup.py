man_u = ["Van der Sar, Edwin", "O'Shea, John", "Evra, Patrice", "Vidic, Nemanja", "Ferdinand, Rio", "Fletcher, Darren", "Carrick, Micheal", "Park, Ji-sung", "Ronaldo, Cristiano", "Berbatov, Dimitar", "Rooney, Wayne"]

player = input("Enter 2008 Man U Player Name(last, First): ")

player.lower()

#this is the beginning of our conditional statement
if player in man_u:
    #first we will check if they're already in the list and if so removing them
    man_u.remove(player)
    print(f"{player} has been removed.")
else:
    #here if the player doesn't exist we are going to add them
    man_u.append(player)
    print(f"{player} has been added.")

#we will then reprint the updated list
print("Updated List:")
for player in man_u:
    print(player)