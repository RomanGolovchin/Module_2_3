my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
lenght = 0
while True:
    if lenght == len(my_list):
        break
    elif my_list[lenght] > 0:
        print(my_list[lenght])
        lenght += 1
    elif my_list[lenght] <= 0:
        lenght += 1
        continue

