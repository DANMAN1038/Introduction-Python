#Danial Syed
#This function first compares the last two letters, as well as every letter that is next to each other and adds to a counter and if that counter is = to the max_repeat, then it adds that letter to a new list
#This functions takes in a phrase which is a string and a max_repeat which checks 
#A list of flagged letters are returned
def flag_keys(phrase, max_repeat):
    #Splits words into letters
    seperated = phrase.split()
    flagged = []
    counter = 1
    for letters in seperated:
        #Compares last two letters for similarity since the next for loop doesn't go over the last letter
        if letters[-1] == letters[-2]:
                counter += 1
                flagged += letters[-1]
        #Compares each letter with the next and adds it to the list if it is = to the max_repeat        
        for j in range(len(letters)-1):
            if letters[j] == letters[j + 1]:
                counter += 1
                if counter == max_repeat:
                    flagged += letters[j]
    return flagged
if __name__ == '__main__':
    print(flag_keys('Heeeellooo Wooorllld', 3))
    print(flag_keys('Heeeellllllooo Okay', 3))
