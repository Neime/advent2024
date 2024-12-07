from collections import Counter

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

    rightCount = Counter(rightList)
    
    res = sum(i * rightCount[i] for i in leftList if i in rightCount)
            
    print(res)
if __name__ == '__main__':
    main()
