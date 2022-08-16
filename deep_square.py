def deep_square(lst):
    if lst == []:
        return []
    elif type(lst) == int:
        return lst**2
    else:
        return [deep_square(lst[0])] + deep_square(lst[1:])
print(deep_square([[-1,[2],[3],[[[-4,5]]],[],[]]])) 
