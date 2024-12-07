def read_puzzle_file(file_path):
    puzzle = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            puzzle.append(row)
    return puzzle
        
def is_ok(row):
    supOrInf = None
    for index in range(len(row) - 1):
        i = row[index]
        next_i = row[index + 1]
        
        if abs(i - next_i) > 3:
            break

        state = 'sup' if i > next_i else 'inf' if i < next_i else 'eq'
        if state == 'eq':
            break

        if supOrInf is None:
            supOrInf = state
            
        if supOrInf != state:
            break
    else:
        return True

    return False

def is_ok_with_dampener(row):
    for i in range(len(row)):
        temp_row = row[:i] + row[i+1:]
        if is_ok(temp_row):
            return True
    return False

def main():
    puzzle = read_puzzle_file('day2/puzzle.txt')

    res = 0
    for row in puzzle:
        if is_ok(row) or is_ok_with_dampener(row):
            res += 1                

    print(res)
            
if __name__ == '__main__':
    main()
