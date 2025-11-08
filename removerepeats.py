numbers = [1, 2, 2, 3, 4, 4, 5]

# Method to remove duplicates while preserving order
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)

# Alternative method using set
# unique_numbers = list(set(numbers))
# print(unique_numbers)