input_rows = int(input("Enter the number of rows : "))
list_of_lists = []
diagonals1 = 0
diagonals2 = 0

def Create_List_of_Lists():
    global list_of_lists
    for new_row in range(input_rows):
        input_int_list = list(map(int, input(
            "Enter the integer elements of list(Space-Separated): ").strip().split()))[:input_rows]
        list_of_lists.append(input_int_list)

def Calculate_Diagonals():
    global input_rows
    global diagonals1
    global diagonals2
    row_count = 0
    for row in list_of_lists:
        diagonals1 += int(row[row_count])
        diagonals2 += int(row[input_rows-row_count-1])
        row_count += 1

def Calculate_diffrens():
    global diagonals1
    global diagonals2
    return diagonals1 - diagonals2

Create_List_of_Lists()
Calculate_Diagonals()
print('The sum diagonal1 = ', diagonals1)
print('The sum diagonal2 = ', diagonals2)
print('differens: ', Calculate_diffrens())
