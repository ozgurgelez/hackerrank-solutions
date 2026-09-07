def minion_game(string):
    vowels = "AEIOU"
    kevin = 0
    stuart = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin += (length - i)
        else:
            stuart += (length - i)

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")