def task_1(values):
    points = {'X' : 1, 'Y' : 2, 'Z' : 3}
    
    win, draw, loss = 6, 3, 0
    score = 0
    # A, X = Rock
    # B, Y = Paper
    # C, Z = Scissors
    for value in values:
        opponent, me = value.strip().split(' ')
        score += points.get(me)
        if (opponent == 'A' and me == 'X') or (opponent == 'B' and me == 'Y') or (opponent == 'C' and me == 'Z'):
            score += draw
            
        elif (opponent == 'A' and me == 'Y') or (opponent == 'B' and me == 'Z') or (opponent == 'C' and me == 'X'):
            score += win

            
    return score

def task_2(values):
    # A= Rock
    # B = Paper
    # C = Scissors
    # X = lose
    # Y = draw
    # Z = win
    
    order = ['A', 'B', 'C', 'A', 'B']
    points_move = {'A' : 1, 'B' : 2, 'C' : 3}
    points_result = {'X' : 0, 'Y' : 3, 'Z' : 6}
    score = 0
    
    for value in values:
        move, result = value.strip().split(' ')
        score += points_result.get(result)
        if result == 'X': # Loss
            move = order[order.index(move) + 2]
        elif result == 'Z': # Win
            move = order[order.index(move) + 1]
        
        score += points_move.get(move)
        
    return score



input = open('input.txt', 'r')
values = input.readlines()
print(task_1(values))
print(task_2(values))