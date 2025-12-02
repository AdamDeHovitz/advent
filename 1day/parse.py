count = 50
ret = 0
with open("full") as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        right = 'R' == line[0]
        num = int(line[1:])
        if right:
            total = count + num
            ret += int(total / 100)
            count = total % 100
        elif count >= num:
            count -= num
            if count == 0:
                ret += 1
        else:
            total = count - num
            if (count != 0):
                ret += 1
            ret += abs(int(total / 100)) 
            count = total % 100
        print(line + " " + str(count))
print(ret)
