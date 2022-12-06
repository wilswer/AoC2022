from __future__ import annotations


def solution() -> int:
    with open("day6/input.txt") as f:
        content = f.read()
    for i in range(len(content)):
        if len(set(content[i : i + 4])) == 4:
            return i + 4
    return -1


if __name__ == "__main__":
    print(solution())
