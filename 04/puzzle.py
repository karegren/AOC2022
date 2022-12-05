def task_1(values):
    score = 0
    
    for line in values:
        first_elf, second_elf = line.strip().split(',')
        first_range = list(range(int(first_elf.split('-')[0]), int(first_elf.split('-')[1]) + 1))
        second_range = list(range(int(second_elf.split('-')[0]), int(second_elf.split('-')[1]) + 1))
        if set(first_range).issubset(second_range):
            score += 1
        elif set(second_range).issubset(first_range):
            score += 1
    
    return score

def task_2(values):
    score = 0
    
    for line in values:
        first_elf, second_elf = line.strip().split(',')
        first_range = list(range(int(first_elf.split('-')[0]), int(first_elf.split('-')[1]) + 1))
        second_range = list(range(int(second_elf.split('-')[0]), int(second_elf.split('-')[1]) + 1))
        if set(first_range).intersection(second_range):
            score += 1
        elif set(second_range).intersection(first_range):
            score += 1
    
    return score

input = open('input.txt', 'r')
values = input.readlines()
print(task_1(values))
print(task_2(values))

