from __future__ import annotations


def complete_overlap(
    first_range: tuple[int, ...], second_range: tuple[int, ...]
) -> bool:
    first_overlap = (first_range[0] <= second_range[0]) and (
        first_range[1] >= second_range[1]
    )
    second_overlap = (first_range[0] >= second_range[0]) and (
        first_range[1] <= second_range[1]
    )
    return first_overlap or second_overlap


def solution() -> int:
    with open("day4/input.txt") as f:
        content = f.read()
    lines = content.split("\n")
    ranges = [line.split(",") for line in lines]
    overlap_count = 0
    for range_pair in ranges:
        range_pair_tuples = [
            tuple([int(num) for num in r.split("-")]) for r in range_pair
        ]
        first_range, second_range = range_pair_tuples
        if complete_overlap(first_range, second_range):
            overlap_count += 1

    return overlap_count


if __name__ == "__main__":
    print(solution())
