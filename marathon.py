#Danial Syed
#This function opens a file with two columns of names and numbers. Each of these are their own element and we look for which string matches that element, then we find out the element next to it to get the number of miles that person ran
#The input parameters are the name of the file and a string which is the member we are looking for
#The final number of miles ran by the member
def miles_run(file_name, member):
    try:
        fp = open(file_name, 'r')
        lines = fp.readlines()
        total = 0
        for ele in lines:
            newLines = str(ele).split(',')
            for ele in newLines:
                #Checks if the first index(name) is the same as a member
                if newLines[0] == member:
                    #Adds the second index(miles ran) to a total which keeps track of how many that individual ran
                    total += int(newLines[1])
                #Will stop the for loop and just return 0 if member is not found
                else:
                    return 0
        #The for loop before this loops around twice, halve the total and that gives me how many miles they actually ran
        final = total / 2
        return(final)
    except FileNotFoundError:
        return -1
#miles_run('week1.csv', 'Sam')
