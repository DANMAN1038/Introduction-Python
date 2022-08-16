#Danial Syed
#This function counts all non float and int elements in a list
#The input_list parameter is a list with elements such as strings, ints, floats, tuples, and lists or nothing
#This function returns either 0 if there is nothing in the list or it is an int or float, 1 if there is a single string or empty tuple, or returns a recursion of going through each element in a list and counts how many there are
def count_non_numbers(input_list):
    #If the input list is empty, return 0
    if input_list == [] or input_list == ():
        return 0
    elif type(input_list[0]) == str:
        return 1 + count_non_numbers(input_list[1:])
    elif type(input_list[0]) == list or type(input_list[0]) == tuple:
        return 1 + count_non_numbers(input_list[0]) + count_non_numbers(input_list[1:])
    else:
    #recursive call for any list or tuple with elements and checks to see how many there are(if one is in another)
        return count_non_numbers(input_list[1:])
print(count_non_numbers([[], [[]]]))
