def find_longest_consecutive_sequence(nums_set):
    nums = set(nums_set)
    max_length = 0
    longest_sequence = []
    
    for num in nums:
        if num - 1 not in nums:
            current_num = num
            current_sequence = [current_num]
            while current_num + 1 in nums:
                current_num += 1
                current_sequence.append(current_num)
            if len(current_sequence) > max_length:
                max_length = len(current_sequence)
                longest_sequence = current_sequence
    
    return max_length, longest_sequence

sample_input = {100, 4, 200, 1, 3, 2}
length, sequence = find_longest_consecutive_sequence(sample_input)
print(f"The longest consecutive sequence is {set(sequence)}.")
