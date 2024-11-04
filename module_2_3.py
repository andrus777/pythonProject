my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i_ = 0
while i_ < len(my_list):
    if my_list[i_] > 0:
        print(my_list[i_])
        i_ += 1
    elif my_list[i_] == 0:
        i_ += 1
        continue
    else:
        break
