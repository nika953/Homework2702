games = []
game = input("Введите игру: ")
while game != "0":
    if game in games:
        print("Эта игра уже записана")
    else:
        games.append(game)
    game = input("Введите игру: ")
games.sort()
print(games)