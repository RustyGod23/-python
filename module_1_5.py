immutable_var = 1, "rock", True
print(immutable_var)
# immutable_var[0] = 2 на данном этапе программа выдаёт ошибку, так как объект "immutable_var" относится к неизменяемому типу списков.
mutable_list = [27, "rock", True]
mutable_list[0] = 30
mutable_list[1] = "hard"
mutable_list[2] = False
print(mutable_list)