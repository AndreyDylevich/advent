score_num_shape = 0
score_win = 0
total = 0



with open ("day2.txt") as f:

    strategies = f.read().strip().lower()

    points = strategies.split("\n")

    for i in points:
        game = i.split()
        if game[1] == "x":
            score_num_shape = 1
        elif game[1] == "y":
            score_num_shape = 2
        else:
            score_num_shape = 3

        if game[0] == "a":
            if game[1] == "x":
                score_win = 3 + score_num_shape
            elif game[1] == "y":
                score_win = 6 + score_num_shape
            else:
                score_win = 0 + score_num_shape

        elif game[0] == "b":
            if game[1] == "x":
                score_win = 0 + score_num_shape
            elif game[1] == "y":
                score_win = 3 + score_num_shape
            else:
                score_win = 6 + score_num_shape

        elif game[0] == "c":
            if game[1] == "x":
                score_win = 6 + score_num_shape
            elif game[1] == "y":
                score_win = 0 + score_num_shape
            else:
                score_win = 3 + score_num_shape

        total = total + score_win


    print(total)

# part 2
score_num_shape2 = 0
score_win2 = 0
total2 = 0
with open("day2.txt") as f:
    strategies2 = f.read().strip().lower()
    points2 = strategies2.split("\n")

for i in points2:

    game2 = i.split()

    if game2[1] == "x":
        score_num_shape2 = 0
    elif game2[1] == "y":
        score_num_shape2 = 3
    else:
        score_num_shape2 = 6

    if game2[0] == "a":
        if game2[1] == "x":
            score_win2 = 3 + score_num_shape2
        elif game2[1] == "y":
            score_win2 = 1 + score_num_shape2
        else:
            score_win2 = 2 + score_num_shape2

    if game2[0] == "b":
        if game2[1] == "x":
            score_win2 = 1 + score_num_shape2
        elif game2[1] == "y":
            score_win2 = 2 + score_num_shape2
        else:
            score_win2 = 3 + score_num_shape2

    if game2[0] == "c":
        if game2[1] == "x":
            score_win2 = 2 + score_num_shape2
        elif game2[1] == "y":
            score_win2 = 3 + score_num_shape2
        else:
            score_win2 = 1 + score_num_shape2

    total2 = total2 + score_win2

print(total2)
