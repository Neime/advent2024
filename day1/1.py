def read_puzzle_file(file_path):
    puzzle = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            puzzle.append(row)
    return puzzle
        
def main():
    puzzle = read_puzzle_file('day1/puzzle.txt')

    leftList = [row[0] for row in puzzle]
    rightList = [row[1] for row in puzzle]


    res = sum(abs(sorted(rightList)[i] - number) for i, number in enumerate(sorted(leftList)))

    print(res)
            
if __name__ == '__main__':
    main()
