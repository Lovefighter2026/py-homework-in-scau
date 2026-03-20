def find_number_index(numbers, target):
    for i, num in enumerate(numbers, start=1):
        if num == target:
            return i
    return 0

if __name__ == "__main__":
    first_line = input().strip()
    numbers_str = first_line.strip('[]') 
    numbers = list(map(int, numbers_str.split()))
    target = int(input().strip())

    position = find_number_index(numbers, target)

    print(position)
