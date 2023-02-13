"""
from statistics import mean

number_list = []
while True:
    try:
        number = input("enter a number: ")
        if :
            break
        number_list.append(number)
    except ValueError as e:
        print(e)

print(mean(number_list))
"""



def sum_of_integer(list_val):
    return sum(list_val)

values = []
while True:
    try:
        integer = int(input("enter an integer: "))
        values.append(integer)
    except ValueError:
        print("enter a integer value")

print(sum_of_integer(values))
