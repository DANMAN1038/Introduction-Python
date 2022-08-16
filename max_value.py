def max_value(lst):
    if lst == []:
        return 0
    elif lst[0] > max_value(lst[1:]):
        return(lst[0])
    else: 
        return max_value(lst[1:])
print(max_value([10, 7, 4, 13, 11]))
