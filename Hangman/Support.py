#Module Support


def find_in_string(word, target):
    locations = []
    for c in range(len(word)):
        if word[c] == target:
            locations.append(c)
    return locations


def unite(a, b):
    c =[]

    for x in a:
        if not(x in c):
            c.append(x)
    for x in b:
        if not(x in c):
            c.append(x)
    return c


def draw(file_name):
    f = open(file_name, "r")
    print(f.read())





    
    
        
