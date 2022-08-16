#Danial Syed
#This function searches through the values of a dictionary and automatically sets the first term as the max and min, then we compare the rest of the values within that list to see if they are larger or smaller and that number is that added to a new dicitonary along with the previous keys
#A dictionary is inputed which can either be empty or have keys with values
#A new dictionary is return (new_dict) which is made up of the original keys as well as the minimum and maximum values for each key
def min_max_hours(emp_diction):
    new_dict = {}
    #if the dictionary is completely empty, then an empty list is returned
    if emp_diction == []:
        return []
    else:
        for i in emp_diction:
            new_list = []
            #If there is a value with an empty list, then it returns value as (0,0)
            if emp_diction[i] == []:
                new_dict[i] = (0,0)
                return new_dict
            else:
                #Sets first value as the max and min
                max_number = emp_diction[i][0]
                min_number = emp_diction[i][0]
                #Compares first ele and the rest ele and determines which is biggest and smallest
                for ele in emp_diction[i]:
                    if ele > max_number:
                        max_number = ele
                    elif ele < min_number:
                        min_number = ele
            #Adds max and min number to a new list which is added to a new dictionary
            new_list.append(min_number)
            new_list.append(max_number)
            new_dict[i] = new_list
    return new_dict
print(min_max_hours({"Shana": [20], "Jody": [10, 20, 10, 5], "Mike": [40, 40]}))
