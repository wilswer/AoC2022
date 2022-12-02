def solution() -> None:
    with open("day1/input.txt") as f:
        lines = f.readlines()
        lines = [int(l.strip("\n")) if l != "\n" else l for l in lines]
        cumsums = []
        s = 0
        for l in lines:
            if l != "\n":
                s += l
            else:
                cumsums.append(s)
                s = 0
    cumsums.sort()
    return sum(cumsums[-3:])


if __name__ == "__main__":
    print(solution())
