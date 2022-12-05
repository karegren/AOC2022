from collections import deque
from collections import defaultdict

def task_1(values):
    values = [line.rstrip() for line in values]
    stacks = {"1": deque([]),
              "2": deque([]),
              "3": deque([]),
              "4": deque([]),
              "5": deque([]),
              "6": deque([]),
              "7": deque([]),
              "8": deque([]),
              "9": deque([])}
    for line in values:
        if line.startswith('move'):
            moves = line.split(' ')
            for _ in range(int(moves[1])):
                top = stacks.get(moves[3]).popleft()
                stacks.get(moves[5]).appendleft(top)
            
        elif not line.startswith(' 1'):
            for index, letter in enumerate(line[1::4]):
                if letter != " ":
                    index += 1
                    stacks.get(str(index)).append(letter)
    
    top_of_stacks = [x[0] for x in list(stacks.values())]
    return "".join(top_of_stacks)
    
def task_2(values):
    values = [line.rstrip() for line in values]
    stacks = {"1": deque([]),
              "2": deque([]),
              "3": deque([]),
              "4": deque([]),
              "5": deque([]),
              "6": deque([]),
              "7": deque([]),
              "8": deque([]),
              "9": deque([])}
    for line in values:
        if line.startswith('move'):
            moves = line.split(' ')
            temp = []
            for _ in range(int(moves[1])):
                top = stacks.get(moves[3]).popleft()
                temp.append(top)
            for letter in reversed(temp):
                stacks.get(moves[5]).appendleft(letter)
                
            
        elif not line.startswith(' 1'):
            for index, letter in enumerate(line[1::4]):
                if letter != " ":
                    index += 1
                    stacks.get(str(index)).append(letter)
    
    top_of_stacks = [x[0] for x in list(stacks.values())]
    return "".join(top_of_stacks)

input = open('input.txt', 'r')
values = input.readlines()
print(task_1(values))
print(task_2(values))

