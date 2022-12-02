hand_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
shape_score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
outcome = {
    ("rock", "paper"): "win",
    ("paper", "scissors"): "win",
    ("scissors", "rock"): "win",
    ("paper", "rock"): "loss",
    ("scissors", "paper"): "loss",
    ("rock", "scissors"): "loss",
    ("rock", "rock"): "tie",
    ("paper", "paper"): "tie",
    ("scissors", "scissors"): "tie",
}


def solution() -> None:
    with open("day2/input.txt") as f:
        content = f.read()
    lines = content.split("\n")
    score = 0
    for line in lines:
        choices = line.split(" ")
        opp_choice = hand_map[choices[0]]
        choice = hand_map[choices[1]]
        game = (opp_choice, choice)
        score += shape_score[choice]
        if outcome[game] == "win":
            score += 6
        if outcome[game] == "tie":
            score += 3
    return score


if __name__ == "__main__":
    print(solution())
