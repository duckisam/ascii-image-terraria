def find_anyIndex(lst, target, ind):
    indices = [i for i, value in enumerate(lst) if value == target]
    return indices[ind -1] if len(indices) > 1 else None

# Example usage
my_list = ['a', 'b', 'c', 'a', 'd', 'b','a','b']
target_letter = 'b'
result = find_anyIndex(my_list, target_letter,3)
print(result)  # Output: 5
