my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
starting_value = 0
while starting_value < len(my_list):
    if my_list[starting_value] >= 1:
        print(my_list[starting_value])
        starting_value += 1
    elif my_list[starting_value] == 0:
        starting_value += 1
        continue
    else:
        break
