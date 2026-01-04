from shlex import join


def mergeIntervals(intervals: list[list[int]]) -> list[list[int]]:
    ret: list[list[int]] = []
    intervals.sort()
    for interval in intervals:
        if ret == []:
            ret.append(interval)
        else:
            currentEnd = ret[len(ret) - 1][1]
            if interval[0] <= currentEnd:
                ret[len(ret) -1][1] = max(currentEnd, interval[1])
            else:
                ret.append(interval)
    return ret

def getActive(intervals: list[list[int]], targets: list[int]): 
    i = 0
    for interval in intervals:
        i = i + interval[1] - interval[0] + 1
    return i    
def parse(filename):
    with open(filename) as f:
        sections = f.read().strip().split("\n\n")
        intervals = [list(map(int, line.split("-"))) for line in sections[0].splitlines()]
        ids = [int(line) for line in sections[1].splitlines()]
        merged= mergeIntervals(intervals)
        #print("Intervals: " + str(merged))
        #print("Targets : " + str(ids))
        print(getActive(merged, ids))
if __name__ == "__main__":
    import sys
    input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/full"
    parse(input_file)
