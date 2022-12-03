import string

letters = string.ascii_lowercase + string.ascii_uppercase
priority = {l: i for i, l in enumerate(letters, start=1)}


def solution() -> int:
    with open("day3/input.txt") as f:
        content = f.read()
    lines = content.split("\n")
    groups = [tuple(lines[i : i + 3]) for i in range(0, len(lines), 3)]
    common_item = [set(group[0]) & set(group[1]) & set(group[2]) for group in groups]
    priorities = [priority[next(iter(item))] for item in common_item]
    return sum(priorities)


if __name__ == "__main__":
    print(solution())
