f = open("inputs.txt", "r")

data = f.read()

def contains(data, value):
    found = False
    for o in data:
        if o == value: 
            found = True
            break
    return found

def compute(data):
    occurences = []
    frequency = 0
    reachTwice = False
    while (not reachTwice):
        for i in data.split('\n'):
            modifier = i.strip()
            if modifier[0:1] == '+':
                frequency += int(modifier[1:])
            elif modifier[0:1] == '-':
                frequency -= int(modifier[1:])
            if contains(occurences, frequency):
                print('occured twice : ' + str(frequency))
                reachTwice = True
                break
            occurences.append(frequency)    
    return frequency

result = compute(data)
print('frequency found : ' + str(result))