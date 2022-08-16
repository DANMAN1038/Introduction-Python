#Danial Syed
#This function searches if an element(names) is in every sublist(clubs). If it is, it adds that element to a new list which will be returned
#The parameter clubs takes in every sublist of the which is inputed
#A new list is returned which includes all the names(busybodies) which were in all of the sublists
def busybody(clubs):
    busybody = []
    #Goes through each element(names) in list of clubs
    for names in clubs[0]:
        busybody_a = True
        for i in range(len(clubs)):
            if names not in clubs[i]:
                #Stops if names is not in every clubs
                busybody_a = False
        if busybody_a == True:
            #Adds names to new list busybody if it is in every list
            busybody.append(names)
    return busybody
print(busybody([['Evans','Hemsworth','Pine','Pratt','Rock'], ['Elba','Hemsworth','Pine','Quinto','Saldana'], ['Gadot','Pascal','Pine','Wiig']]))
