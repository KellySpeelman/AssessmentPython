import random
def get_number():
    while True:
        try:
            return int(input("Enter the number of rows : "))
        except ValueError:
            print("That was not a number")


input_rows = get_number()
list_of_lists = []
diagonals1 = 0
diagonals2 = 0

def create_List_of_Lists():
    global list_of_lists
    for new_row in range(input_rows):
        input_int_list = create_List()
        list_of_lists.append(input_int_list)
        print(input_int_list)


def create_List():
    list_of_numbers = []
    for x in range(input_rows):
        random_number = random.randrange(-100, 100)
        list_of_numbers.append(random_number)

    return list_of_numbers


    # while True:
    #     try:
    #         return list(map(int, input(
    #             "Enter the integer elements of list(Space-Separated): ").strip().split()))[:input_rows]
    #     except ValueError:
    #         print("That was not a number")


def calculate_Diagonals():
    global input_rows
    global diagonals1
    global diagonals2
    row_count = 0
    for row in list_of_lists:
        diagonals1 += int(row[row_count])
        diagonals2 += int(row[input_rows-row_count-1])
        row_count += 1


def calculate_diffrens():
    global diagonals1
    global diagonals2
    return diagonals1 - diagonals2

create_List_of_Lists()
calculate_Diagonals()
print('The sum diagonal1 = ', diagonals1)
print('The sum diagonal2 = ', diagonals2)
print('differens: ', calculate_diffrens())
