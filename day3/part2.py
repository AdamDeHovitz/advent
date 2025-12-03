def getJoltage(bank: str) -> int:
    reversedAns = []
    for c in bank[::-1]:
        num = int(c)
        reversedAns.append(num)
        if len(reversedAns) > 12:
            mI = 0  # default: remove least significant
            for i in range(len(reversedAns) - 1, 0, -1):
                if reversedAns[i] < reversedAns[i - 1]:
                    mI = i
                    break
            del reversedAns[mI]

    return int("".join(map(str, reversedAns[::-1])))


with open("inputs/full") as file:
    lines = [line.rstrip() for line in file]
    num = 0
    for line in lines:
        result = getJoltage(line)
        print(line + ": " + str(result))
        num += result
    print(num)
