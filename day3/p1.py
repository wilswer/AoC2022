import string

letters = string.ascii_lowercase + string.ascii_uppercase
priority = {l: i for i, l in enumerate(letters, start=1)}


def solution() -> int:
    with open("day3/input.txt") as f:
        content = f.read()
    lines = content.split("\n")
    halves = [(line[: len(line) // 2], line[len(line) // 2 :]) for line in lines]
    common_item = [set(halve[0]) & set(halve[1]) for halve in halves]
    priorities = [priority[next(iter(item))] for item in common_item]
    return sum(priorities)


if __name__ == "__main__":
    print(solution())
