# Strategy
# Sort intervals and create merged intervals
# Sort ingredients
# Iterate through the merged intervals. For each interval, if the
# head of ingredients is in the current interval, pop to success, else if it's less than current interval trash, else continueinue

from shlex import join


def mergeIntervals(intervals: list[list[int]]) -> list[list[int]]:
    ret: list[list[int]] = []
    intervals.sort()
    for interval in intervals:
        if ret == []:
            ret.append(interval)
        else:
            currentEnd = ret[len(ret) - 1][1]
            if interval[0] < currentEnd:
                ret[len(ret) -1][1] = max(currentEnd, interval[1])
            else:
                ret.append(interval)
    return ret

def getActive(intervals: list[list[int]], targets: list[int]) -> list[int]:
    ret: list[int] = []
    i = 0
    for interval in intervals:
        #print("Interval: " + str(interval))
        while i < len(targets):
            cur = targets[i]
            #print("Current: " + str(cur))
            if cur < interval[0]:
                i= i + 1
                continue
            if cur <= interval[1]:
                ret.append(cur)
                i = i + 1
                continue 
            break
    return ret    
def parse(filename):
    with open(filename) as f:
        sections = f.read().strip().split("\n\n")
        intervals = [list(map(int, line.split("-"))) for line in sections[0].splitlines()]
        ids = [int(line) for line in sections[1].splitlines()]
        merged= mergeIntervals(intervals)
        ids.sort()
        #print("Intervals: " + str(merged))
        #print("Targets : " + str(ids))
        print(len(getActive(merged, ids)))
if __name__ == "__main__":
    import sys
    input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/full"
    parse(input_file)
