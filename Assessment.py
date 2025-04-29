
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
diagonals1 = 0
diagonals2 = 0

def Calculate_Diagonals():
    global diagonals1
    diagonals1 = int(input_int_list1[0]) + int(input_int_list2[1]) + int(input_int_list3[2])
    global diagonals2
    diagonals2 = int(input_int_list1[2]) + int(input_int_list2[1]) + int(input_int_list3[0])

Calculate_Diagonals()
print('The sum diagonal1 = ', diagonals1)
print('The sum diagonal2 = ', diagonals2)
