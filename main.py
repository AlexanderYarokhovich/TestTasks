def get_unique_sorted(int_list):

    unique_values = []
    for num in int_list:
        if num not in unique_values:
            unique_values.append(num)

    for i in range(len(unique_values)):
        for j in range(len(unique_values) - 1):
            if unique_values[j] > unique_values[j + 1]:
                unique_values[j], unique_values[j + 1] = unique_values[j + 1], unique_values[j]

    return unique_values



numbers = [4, 2, 5, 2, 3, 4, 1]
result = get_unique_sorted(numbers)
print(result)


