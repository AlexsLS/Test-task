import sys
def read_nums(filename):
    nums = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                nums.append(int(line))
    return nums
def min_moves(nums):
    nums_sorted = sorted(nums)
    n = len(nums_sorted)
    median = nums_sorted[n // 2]
    moves = sum(abs(x - median) for x in nums_sorted)
    return moves
def main():
    if len(sys.argv) != 2:
        print("Использование: python script.py nums.txt")
        return
    filename = sys.argv[1]
    nums = read_nums(filename)
    moves = min_moves(nums)
    if moves <= 20:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
if __name__ == "__main__":
    main()
