def getPaper(l, w, h):
    return (2*((l*w) + (w*h) + (l*h)))+(smallestPaper(l, w, h))

def smallestPaper(l, w, h):
    nums = [l, w, h]
    largest = max(nums)
    nums.remove(largest)
    return (nums[0] * nums[1])


def getLineTotal(line):
    l, w, h = line.split('x')
    l = int(l)
    w = int(w)
    h = int(h.strip())

    return (getPaper(l, w, h), getRibbon(l, w, h))

def getRibbon(l, w, h):
    return (2*(smallestRibbon(l, w, h))) + l*w*h

def smallestRibbon(l, w, h):
    nums = [l, w, h]
    largest = max(nums)
    nums.remove(largest)
    return (nums[0] + nums[1])

if __name__ == "__main__":
    f = open('/home/zobal/inputFile', 'r')
    lines = f.readlines()
    f.close
    paper = 0
    ribbon = 0
    for line in lines:
        linePaper, lineRibbon = getLineTotal(line)
        paper += linePaper
        ribbon += lineRibbon

    print paper
    print ribbon