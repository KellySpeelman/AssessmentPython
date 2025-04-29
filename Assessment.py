# import random


def start():
    number_of_rows = get_number()
    list_of_lists = create_list_of_lists(number_of_rows)
    calculated_list = calculate_diagonals(number_of_rows, list_of_lists)
    print('The sum diagonal1 = ', calculated_list[0])
    print('The sum diagonal2 = ', calculated_list[1])
    print('difference: ', calculate_difference(calculated_list))


def get_number():
    while True:
        try:
            return int(input("Enter the number of rows : "))
        except ValueError:
            print("That was not a number")


def create_list_of_lists(number_of_rows):
    list_of_lists = []
    for new_row in range(number_of_rows):
        input_int_list = create_list(number_of_rows, new_row)
        list_of_lists.append(input_int_list)
    print(list_of_lists)
    return list_of_lists


def create_list(number_of_rows, new_row):
    list_of_numbers = []
    for x in range(number_of_rows):
        while True:
            try:
                number = int(input(
                    "Enter the integer for place {} in row {}: ".format(x+1, new_row+1)))
                list_of_numbers.append(number)
                break
            except ValueError:
                print("That was not a number")
    return list_of_numbers


def calculate_diagonals(number_of_rows, list_of_lists):
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    row_count = 0
    for row in list_of_lists:
        left_to_right_diagonal += int(row[row_count])
        right_to_left_diagonal += int(row[number_of_rows-row_count-1])
        row_count += 1
    return [left_to_right_diagonal, right_to_left_diagonal]


def calculate_difference(calculated_list):
    return calculated_list[0] - calculated_list[1]


start()
