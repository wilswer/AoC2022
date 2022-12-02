hand_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}
shape_score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
outcome = {
    "Z": "win",
    "Y": "tie",
    "X": "loss",
}
strategy = {
    "win": [("rock", "paper"), ("paper", "scissors"), ("scissors", "rock")],
    "loss": [("paper", "rock"), ("scissors", "paper"), ("rock", "scissors")],
    "tie": [("paper", "paper"), ("scissors", "scissors"), ("rock", "rock")],
}


def solution() -> None:
    with open("day2/input.txt") as f:
        content = f.read()
    lines = content.split("\n")
    score = 0
    for line in lines:
        choices = line.split(" ")
        opp_choice = hand_map[choices[0]]
        desired_outcome = outcome[choices[1]]
        shape_to_choose = [
            game for game in strategy[desired_outcome] if game[0] == opp_choice
        ]
        score += shape_score[shape_to_choose[0][1]]
        if desired_outcome == "win":
            score += 6
        if desired_outcome == "tie":
            score += 3
    return score


if __name__ == "__main__":
    print(solution())
