players = ['John', 'Mary', 'Tom', 'Lisa']
print(players[0:3])
print(players[1:3])
# print(players[2:10]) # This will give an error as the index is out of range.
print(players[1:])
print(players[:3])
print(players[-3:])
print(players[-4])
print(players[-4:])
print("Here are the first three players in our team: ")
for player in players[:3]:
    print(f"player is {player.title()} !")
print("Here are the last three players in our team: ")
for player in players[-3:]:
    print(f"player is {player.upper()} !")
print("Here are all the players in our team: ")
for player in players:
    print(f"player is {player.lower()} !")
            

