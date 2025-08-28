import random
print("welcome to the goblin game")
print("The best game ever")
player_game = input("Write your name")
print(player_game,"can you find the goblin")
print("|_||_||_||_||_|")
goblin_position = random,randint(1, 5)
Keep_trying = True
while Keep_trying: 
 guessed_position = int(input("can you guess where the goblin is?"))
 if guessed_position == goblin_position:
 print("good luck you find the goblin")
 Keep_trying = False
 else: print("no")
