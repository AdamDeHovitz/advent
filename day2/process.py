def getInvalidNums(start: int, end: int):
    nums = set()
    current = start
    while current <= end:
        strNum: str = str(current)
        base = strNum[len(strNum) // 2 :]
        if base[0] == "0":
            current += 10 ** (len(base) - 1)
            continue
        target = int(base + base)
        # print(str(current) + ": " + str(target))
        if start <= target <= end:
            nums.add(target)
        current += 1
    return list(nums)


def parse_ranges(filename):
    with open(filename, "r") as f:
        content = f.read().replace("\n", "")

    ranges = []
    for range_str in content.split(","):
        range_str = range_str.strip()
        if range_str:  # Skip empty strings
            start, end = range_str.split("-")
            ranges.append((int(start), int(end)))

    return ranges


# Usage:
ranges = parse_ranges("inputs/full")
total = 0
for start, end in ranges:
    total += sum(getInvalidNums(start, end))
print(total)
