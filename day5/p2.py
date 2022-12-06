from __future__ import annotations


def solution() -> str:
    with open("day5/input.txt") as f:
        content = f.read()
    stack_text, instruction_text = content.split("\n\n")
    stack = stack_text.split("\n")
    stack = [s for s in stack]
    n_stacks = int(stack[-1].strip()[-1])
    crates = [c.replace("    ", " X ").strip() for c in stack[:-1]]
    crates_list = [[ci for ci in c.split(" ") if ci != ""] for c in crates]
    stacks: dict[int, list[str]] = {i: [] for i in range(1, n_stacks + 1)}
    for line in crates_list:
        for i in range(1, n_stacks + 1):
            if line[i - 1] != "X":
                stacks[i].append(line[i - 1])
    for key in stacks.keys():
        stacks[key] = stacks[key][::-1]
    instructions = instruction_text.split("\n")
    for instruction in instructions:
        amount, from_, to = [int(i) for i in instruction.split(" ") if i.isnumeric()]
        stacks[to].extend(stacks[from_][-amount:])
        del stacks[from_][-amount:]
    last_letters = []
    for i, stack in stacks.items():
        last_letters.append(stack[-1])
    return "".join(last_letters).replace("[", "").replace("]", "")


if __name__ == "__main__":
    print(solution())
