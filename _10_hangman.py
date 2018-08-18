def hangman(answer_word):

    counter = 0  # Counter of player's mistakes.
    hangman = ["",
            "______      ",
            "|     |     ",
            "|     |     ",
            "|     0     ",
            "|    /|\    ",
            "|    / \    ",
            "|           "
            ]
    answer = list(answer_word)  # List of answer's letters. ["c", "a", "t"]
    answer_player = ["_"] * len(answer_word)  # List of player's letters. ["_", "_", "_"]
    win = False

    print("\n" + "Welcome to HANGMAN!")

    while counter < len(hangman) - 1:  # If mistakes number has not yet achieved last item of hangman List.
        msg = "\n" + "Please predict each letter of a \"word\" (3 letters, an animal)!: "
        input_letter = input(msg)

        if input_letter in answer:  # If there is a letter in answer.
            index_letter = answer.index(input_letter)  # Find the index of the letter in answer_word.
            answer_player[index_letter] = input_letter  # Change an item in "answer_player" from _ to a letter.
            answer[index_letter] = '***'  # Change an item in Answer to avoid duplicated detection.
        else:  # If there is not in answer.
            counter += 1  # Increase the counter of miskake.

        print("\n")
        print("Your answer: " + " ".join(answer_player))  # Your answer: _ _ _
        print("\n".join(hangman[0 : counter + 1]))  # Display HANGMAN based on mistake counter!
        print("\n")

        if "_" not in answer_player:  # If all underscores disapeared.
            print("You won!")
            print(" ".join(answer_player))
            print("\n")
            win = True
            break

    if not win:
        print("GAME OVER ... The correct answer is \"{}\".".format(answer_word))
        print("\n")

hangman("cat")
