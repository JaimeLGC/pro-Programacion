# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:

    player1 = "A"
    player2 = "B"
    points_player1 = points_player2 = 0
    games_player1 = games_player2 = 0
    sets_player1 = sets_player2 = 0
    for point in points:
        if point == "A":
            points_player1 += 1
        else:
            points_player2 += 1

    if points_player1 >= 4 and points_player1 - points_player2 >= 2:
        games_player1 += 1
        points_player1 = points_player2 = 0
    elif points_player2 >= 4 and points_player2 - points_player1 >= 2:
        games_player2 += 1
        points_player1 = points_player2 = 0

    if games_player1 >= 6 and games_player1 - games_player2 >= 2:
        sets_player1 += 1
    elif games_player2 >= 6 and games_player2 - games_player1 >= 2:
        sets_player2 += 1
    elif games_player1 and games_player2 == 6:
        if games_player1 == 7:
            sets_player1 += 1
        elif games_player2 == 7:
            sets_player2 += 1

    if sets_player1 or sets_player2 == 2:
        if sets_player1 == 2:
            winner = player1
        elif sets_player2 == 2:
            winner = player2

    return winner


if __name__ == "__main__":
    run(
        "ABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABAABA"
    )

    """player1 = "A"
    player2 = "B"
    points_player1 = points_player2 = 0
    for point in points:
        if point == "A":
            points_player1 += 1
        else:
            points_player2 += 1

    if points_player1 >= 4 and points_player1 - points_player2 >= 2:
        winner = player1
    elif points_player2 >= 4 and points_player2 - points_player1 >= 2:
        winner = player2
    return winner"""

"""player1 = 0
    player2 = 0
    win = ""
    deuce = False
    for point in points:
        if point == "A":
            player1 += 1
        else:
            player2 += 1
    if player1 == 4 and player2 <= 2:
        win = "A"
    elif player2 == 4 and player1 <= 2:
        win = "B"
    if player1 and player2 == 3:
        deuce = True
    while deuce == True:
        if player1 - player2 >= 2:
            win = "A"
        if player2 - player1 >= 2:
            win = "B"
    else:
        if player1 == 4 and player2 <= 2:
            win = "A"
        if player2 == 4 and player1 <= 2:
            win = "B"
    winner = win"""
