def display_combinations():
    dice_dict = {}
    counter = 1
    matrix = []  
    for i in range(1, 7):
        row = []  
        for j in range(1, 7):
            key = str(counter)
            counter += 1
            value = {"Die_A": i, "Die_B": j, "Sum": i + j}
            dice_dict[key] = value
            row.append(value)  
        matrix.append(row)  

    for row in matrix:
        print(row)

display_combinations()

