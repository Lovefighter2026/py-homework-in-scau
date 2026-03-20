def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    input_str = input().strip()
    if input_str: 
        input_list = input_str.split()
        input_list = [int(x) for x in input_list]
    else:
        input_list = []
    
    result_list = remove_duplicates(input_list)
    
    print(" ".join(str(x) for x in result_list))
