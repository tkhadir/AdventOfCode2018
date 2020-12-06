f = open("inputs.txt", "r")

data = f.read()

def contains(data, value):
    found = False
    for o in data:
        if o == value: 
            found = True
            break
    return found

def getUnique(phrase):
    result = []
    for c in list(phrase):
        if (not contains(result, c)):
            result.append(c)
    return result

def containByOccurence(character, phrase, occurences):
    count = 0
    for c in list(phrase):
        if (character == c):
            count+=1
    return (count == occurences)

def compute(data):
    countTwice = 0
    countThreeTimes = 0
    for d in data.split('\n'):
        checkedThree = False
        checkedTwice = False
        for c in getUnique(d):
            if (containByOccurence(c, d, 3) and (not checkedThree)):
                countThreeTimes+=1
                checkedThree = True
            elif (containByOccurence(c, d, 2) and (not checkedTwice)):
                countTwice+=1
                checkedTwice = True
    return (countTwice * countThreeTimes)

print('found : ' + str(compute(data)))
