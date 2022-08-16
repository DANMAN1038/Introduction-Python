#Danial Syed
#This function contains three for loops, one for each element being added, if each element from each loop is added and the sum is = to the target sum, then we print those three elements
#The parameters of this function are num_list which is a list of inputed integers and target which is the sum we are trying to achieve with the num_list provided
#The triple_count is returned which is the number of possible combinations, inside the last if statement also has a print function which lists out each combination
def triples(num_list, target):
    triple_count = 0
    #First addend
    for i in range(len(num_list)):
        #Second addend
        for j in range(len(num_list)):
            #Third Addend
            for k in range(len(num_list)):
                #Makes sure the different addends are distinct, as well as are in order from least to greatest
                if num_list[j] > num_list[i] and num_list[k] > num_list[j] and num_list[i] + num_list[j] + num_list[k] == target:
                    print("{}+{}+{}={}".format(num_list[i], num_list[j], num_list[k], target))
                    triple_count += 1
    return triple_count
print(triples([6, 5, 0, 1, -4, 4, -1], 10))
