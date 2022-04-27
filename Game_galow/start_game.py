import random
words = ("питон", "гусь", "интернет", "поездка", "теория", "изюм",)


def start():
    """
    start the game
    :return: None
    """
    if input("Приветствую! Хочешь начать игру?\n").lower() == "да":
        x = random.randint(0, 5)
        hangman(words[x])
    else:
        while True:
            if input("ну как хочешь. Напиши \"играть\" если захочешь начать.\n").lower() == "играть":
                x = random.randint(0, 5)
                hangman(words[x])
                break
            else:
                continue


def hangman(word):
    """
    game
    :param word: string
    :return: bool
    """
    wrong = 0
    stages = ["",
              "________          ",
              "|                 ",
              "|        |        ",
              "|        0        ",
              "|       /|\       ",
              "|       / \       ",
              "|                 "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Игра началась!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        print("\n")

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            print("Вы угодали.")
        else:
            wrong += 1
            print("Вы не угодали.")
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[:e]))

        if "_" not in board:
            print("Поздравляю, вы выиграли! "
                  "Было загадано слово: " + word)
            win = True
            break

    if not win:
        print("Вы проиграли. "
              "Было загаданно слово: " + word)
    return win
