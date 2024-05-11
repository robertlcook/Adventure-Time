import random
#type: ignore
def begin():
  print("Hello kids, this is your father Bowser.")
  print("The dog needs to be fed, lets play a game. ")
  print('''   
              ─────▐██──────▄█──███──█▄─────██▌─────
              ────▐██▀─────█████████████────▀██▌────
              ───▐██▌─────██████████████─────▐██▌───
              ───████────████████████████────████───
              ──▐█████──██████████████████──█████▌──
              ───████████████████████████████████───
              ────███████▀▀████████████▀▀███████────
              ─────█████▌──▄▄─▀████▀─▄▄──▐█████─────
              ───▄▄██████▄─▀▀──████──▀▀─▄██████▄▄───
              ──██████████████████████████████████──
              ─████████████████████████████████████─
              ▐██████──███████▀▄██▄▀███████──██████▌
              ▐█████────██████████████████────█████▌
              ▐█████─────██████▀──▀██████─────█████▌
              ─█████▄─────███────────███─────▄█████─
              ──██████─────█──────────█─────██████──
              ────█████────────────────────█████────
              ─────█████──────────────────█████─────
              ──────█████────────────────█████──────
              ───────████───▄────────▄───████───────
              ────────████─██────────██─████────────
              ────────████████─▄██▄─████████────────
              ───────████████████████████████───────
              ───────████████████████████████───────
              ────────▀█████████▀▀█████████▀────────
              ──────────▀███▀────────▀███▀──────────''')
begin()
start = input("Do you want to play a game to feed the dog?    \n(Y/N)  ").lower()
if start == "y":
  print('''WooHoo, let's play\n
            ─────────────────────────────▄██▄
            ─────────────────────────────▀███
            ────────────────────────────────█
            ───────────────▄▄▄▄▄────────────█
            ──────────────▀▄────▀▄──────────█
            ──────────▄▀▀▀▄─█▄▄▄▄█▄▄─▄▀▀▀▄──█
            ─────────█──▄──█────────█───▄─█─█
            ─────────▀▄───▄▀────────▀▄───▄▀─█
            ──────────█▀▀▀────────────▀▀▀─█─█
            ──────────█───────────────────█─█
            ▄▀▄▄▀▄────█──▄█▀█▀█▀█▀█▀█▄────█─█
            █▒▒▒▒█────█──█████████████▄───█─█
            █▒▒▒▒█────█──██████████████▄──█─█
            █▒▒▒▒█────█───██████████████▄─█─█
            █▒▒▒▒█────█────██████████████─█─█
            █▒▒▒▒█────█───██████████████▀─█─█
            █▒▒▒▒█───██───██████████████──█─█
            ▀████▀──██▀█──█████████████▀──█▄█
            ──██───██──▀█──█▄█▄█▄█▄█▄█▀──▄█▀
            ──██──██────▀█─────────────▄▀▓█
            ──██─██──────▀█▀▄▄▄▄▄▄▄▄▄▀▀▓▓▓█
            ──████────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
            ──███─────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
            ──██──────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
            ──██──────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
            ──██─────────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
            ──██────────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
            ──██───────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌
            ──██──────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌
            ──██─────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌
            ──██────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌''')
if start == "n": 
  print("But the dog must be fed, he is hungry. c'mon")
else:
  print("You need to type either a Y or an N")

def guessNumber():
      print("Dad is thinking of a number between 1 and 10")
      print("Whoever is the closest to that number wins the           prize")
      print('''
                ⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
                ⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛
                ⬛🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨⬛
                ⬛🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨⬛
                ⬛🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨⬛
                ⬛🟨🟨⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛🟨🟨⬛
                ⬛🟨🟨🟨⬛⬛⬛🟨🟨⬜⬜⬜⬛🟨🟨⬛
                ⬛🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬛⬛🟨🟨⬛
                ⬛🟨🟨🟨🟨🟨⬜⬜⬜⬛⬛⬛🟨🟨🟨⬛
                ⬛🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨⬛
                ⬛🟨🟨🟨🟨🟨⬜⬜⬜🟨🟨🟨🟨🟨🟨⬛
                ⬛🟨🟨🟨🟨🟨⬜⬜⬜⬛🟨🟨🟨🟨🟨⬛
                ⬛🟨🟨🟨🟨🟨⬛⬛⬛⬛🟨🟨🟨🟨🟨⬛
                ⬛🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨⬛
                ⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛
                ⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜''')

numberChoice = int(input("choose your number  "))
randomNumber = random.randint(1, 10)
if numberChoice == randomNumber:
        print(''' You don't have to feed the dog, you win!!!
                    ⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜
                    ⬜⬜⬜⬜⬛🟨⬛⬜⬜⬜⬜
                    ⬜⬜⬜⬛🟨🟨🟨⬛⬜⬜⬜
                    ⬛⬛⬛⬛🟨🟨🟨⬛⬛⬛⬛
                    ⬛🟨🟨🟨⬛🟨⬛🟨🟨🟨⬛
                    ⬜⬛🟨🟨⬛🟨⬛🟨🟨⬛⬜
                    ⬜⬜⬛🟨🟨🟨🟨🟨⬛⬜⬜
                    ⬜⬜⬛🟨🟨🟨🟨🟨⬛⬜⬜
                    ⬜⬛🟨🟨⬛⬛⬛🟨🟨⬛⬜
                    ⬜⬛🟨⬛⬜⬜⬜⬛🟨⬛⬜
                    ⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜''')
elif numberChoice < 1 or numberChoice > 10:
        print(
            str(numberChoice) +
            " is not a number between 1 and 10, try again")
else:
    print(''' You must feed the dog today!!!
              ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⣀⣀⣀⣀⢀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
              ⠀⠀⠀⠀⠀⣀⣰⣿⣿⡻⠟⠋⠉⠉⣻⠟⠉⠉⠉⠛⢯⡛⢿⣿⣷⣤⣀⠀⠀⠀⠀⠀
              ⠀⣠⣴⠾⠛⢋⣿⠟⠋⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠈⠂⣹⣿⡈⠙⠻⢶⣄⡀⠀
              ⣸⠏⠀⠀⠀⣾⣋⣀⣀⡀⠀⠀⠀⢸⠁⠀⠀⢀⣀⣀⣀⡀⠀⠈⠻⣧⠀⠀⠀⠉⠻⣦
              ⢿⡀⠀⣿⣿⠟⣫⣽⣿⣿⣿⣿⣶⣶⣶⡶⠛⣻⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢀⣿
              ⠸⣧⠀⠈⣿⢸⣿⣿⣿⣿⣿⣿⣿⠁⢹⡇⣼⣿⣿⣿⣿⣿⣿⣿⠁⣼⡇⠀⠀⠀⣼⠇
              ⠀⠹⣷⡀⢹⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⠏⠀⣿⡇⠀⣠⡾⠋⠀
              ⠀⠀⠈⢿⣿⢿⡿⠿⠿⣿⠟⠉⠀⠀⠀⠀⠙⠛⢿⡿⠿⠛⠉⠀⠀⡿⣷⣾⠏⠀⠀⠀
              ⠀⠀⠀⠈⠋⠘⣷⠀⢀⡿⢰⣾⣟⣛⣿⣿⣷⡄⠀⢻⣆⠀⠀⠀⢰⡇⠘⠋⠀⠀⠀⠀
              ⠀⠀⠀⠀⠀⠀⠹⣧⣼⠃⠈⣧⣼⣿⣇⣈⣿⠃⠀⠀⣿⣀⣀⣴⠟⠁⠀⠀⠀⠀⠀⠀
              ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣆⠀⠈⠙⢿⡛⠉⠁⠀⠀⣠⡿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
              ⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡿⢶⣶⣾⣿⣶⣤⣤⣶⢿⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⡼⠁⠉⠏⠁⠈⢹⣠⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⣸⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣤⣤⣤⡾⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⢶⣾⣶⠾⠛⠁''')
print("your number was " + str(numberChoice))
print("and the correct number was " + str(randomNumber))