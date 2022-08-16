#Danial Syed
#The helper function simply adds a variable counter which keeps track of how many times we need to multiply, the nth_base_seq function does the actual math and return all the products
#The three total inputs are base which is how much we want to multiply by, n is how many times we multiply, and the counter which keeps track of how many times we have multiplied
#If the base is less than or = to 0 or if n is less than 0 we return 0, if not we return the recursion of multiplying base n amount of times, the second function returns the counter along with the original inputs of base and n
def nth_base_seq(base, n):
    #base case to see if base is larger than 0 and n is larger or = to 0
    if base <= 0 or n < 0:
        return 0
    else:
        return helper(base, n, [], 0, 0)
#Helper function used to add new variable counter which keeps track of how many times multiplcation has been done
def helper(base, n, out, z, value):
    if not (z < n+1):
        return out
    else:
        if value == 0:
            out.append(1)
            value += 1
            z += 1
        else:
            value = value * base
            out.append(value)
            z += 1
        return helper(base, n, out, z, value)
print(nth_base_seq(3, 10))
