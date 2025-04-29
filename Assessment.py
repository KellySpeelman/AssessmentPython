input_rows = int(input("Enter the number of rows : "))

input_int_list1 = list(map(int, input(
    "Enter the integer elements of list(Space-Separated): ").strip().split()))[:input_rows]
print("array:", input_int_list1)
input_int_list2 = list(map(int, input(
    "Enter the integer elements of list(Space-Separated): ").strip().split()))[:input_rows]
print("array:", input_int_list2)
input_int_list3 = list(map(int, input(
    "Enter the integer elements of list(Space-Separated): ").strip().split()))[:input_rows]
print("list:", input_int_list3)
list_of_lists = [input_int_list1, input_int_list2, input_int_list3]
diagonals1 = 0
diagonals2 = 0

def Calculate_Diagonals():
    global input_rows
    global diagonals1
    global diagonals2
    row_count = 0
    for row in list_of_lists:
        diagonals1 += int(row[row_count])
        diagonals2 += int(row[input_rows-row_count-1])
        row_count += 1
        print('1: ', diagonals1)
        print('2: ', diagonals2)

def Calculate_diffrens():
    global diagonals1
    global diagonals2
    return diagonals1 - diagonals2

Calculate_Diagonals()
print('The sum diagonal1 = ', diagonals1)
print('The sum diagonal2 = ', diagonals2)
print('differens: ', Calculate_diffrens())
