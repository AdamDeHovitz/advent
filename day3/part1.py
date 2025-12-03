def getJoltage(bank: str) -> int:
    max1 = 0
    max2 = 0
    for c in bank:
        num = int(c)
        # print(c + ": " + str(max1) + " " + str(max2))
        if max1 < 10:
            if num > max1:
                max2 = max1 * 10 + num
                max1 = num
            else:
                max1 = max1 * 10 + num
                max2 = max2 // 10 * 10 + num
        else:
            if num > max1 // 10:
                max2 = max1 // 10 * 10 + num
                max1 = num
            else:
                if num > max1 % 10:
                    max1 = max1 // 10 * 10 + num
    return max(max1, max2)


with open("inputs/full") as file:
    lines = [line.rstrip() for line in file]
    num = 0
    for line in lines:
        result = getJoltage(line)
        # print(line + ": " + str(result))
        num += result
    print(num)
