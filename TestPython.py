# num1 = float(input("typ een nummer: "))
# num2 = int(input("typ een nummer: "))
#
# sum = num1 + num2
#
# print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

input_int_array = [int(x) for x in input("Enter the integer elements of list(Space-Separated): ").split()]

print("array:", input_int_array)


# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map, split and strip functions
lst = list(map(int, input(
    "Enter the integer elements of list(Space-Separated): ").strip().split()))[:n]
print('The list is:', lst)   # printing the list

