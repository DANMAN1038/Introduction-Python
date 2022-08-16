#Danial Syed
#This function takes a number and while that number is greater than 0, it will continue to operate for every digit. It takes the modulus of 5 from the number 
#The parameter is the inputed base 10 integer
#The base five version of the base 10 integer is returned
def base_five(num):
    #Since we need to return as string, we start it off as one as well
    num_five = '"'
    count = 0
    while num > 0:
        #Takes the remainder of num / 5 and converts it into a string, so it can be added and compatible with num_five
        num_five = str(num % 5) + num_five 
        #Allows the while loop to keep running once num = num/5(base_five)
        num = int(num / 5)
    #Since I am adding str(num % 5) to the front of the string(before the last quotation), I need to add another quotation before num_five.
    return '"' + num_five
print(base_five(33))
