numbers = [0, 2, 5, 7, 10, 0, 15, 20, 0]

def find_num(list, number):
    target = []

    for index, value in enumerate(list):
        if value == number:
            target.append(index)
    return target

print(find_num(numbers, 0))