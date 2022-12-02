def task_1(values):
    temp_calories = 0
    max_calories = 0
    for val in values:
        if val == '\n':
            if temp_calories > max_calories:
                max_calories = temp_calories    
            temp_calories = 0
            continue
        temp_calories += int(val.strip())
        
    return max_calories

def task_2(values):
    all_elfs = {}
    temp_calories = 0
    elf_no = 1
    for val in values:
        if val == '\n':
            all_elfs[elf_no] = temp_calories
            temp_calories = 0
            elf_no += 1
            continue
        temp_calories += int(val.strip())
        
            
    return sum(sorted(all_elfs.values(), reverse=True)[:3])


input = open('input.txt', "r")
values = input.readlines()
print(f'Most calories carried is: {task_1(values)}')
print(f'Sum of top 3 carried calories: {task_2(values)}')
