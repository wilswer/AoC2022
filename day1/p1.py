def solution() -> int:
    with open("day1/input.txt") as f:
        content = f.read()
    lines = [[int(num) for num in c.split("\n")] for c in content.split("\n\n")]
    cumsums = []
    for group in lines:
        cumsums.append(sum(group))
    return max(cumsums)


if __name__ == "__main__":
    print(solution())
