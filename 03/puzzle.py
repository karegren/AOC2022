letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def task_1(values):

    score = 0
    for line in values:
        first, second = ''.join(line.strip()[:int(len(line)/2)]), ''.join(line.strip()[int(len(line)/2):])
        not_unique = list(set(first).intersection(second))
        for char in not_unique:
            score += letters.find(char) + 1
        
    return score

def task_2(values):
    values = [x.strip() for x in values]
    groups = [values[x:x+3] for x in range(0, len(values), 3)]
    
    score = 0
    for group in groups:
        badge = set(group[0]).intersection(group[1]).intersection(group[2])
        score += letters.find(badge.pop()) + 1
        
    return score


input = open('input.txt', 'r')
values = input.readlines()
print(task_1(values))
print(task_2(values))

