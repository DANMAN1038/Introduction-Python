def translate(text):
    new_list = text.split()
    other_list = []
    for ele in new_list:
        if ele[0] == "A, E, I, O, U, a, e, i, o, u":
            ele=ele+'way'
            other_list.append(ele)
        else:
            word = ele[1:]
            letter = ele[0]
            word=word+letter
            word=word+'ay'
            other_list.append(word)
        something = ' '.join(other_list)
    print(something)
translate("Can you speak pig latin?")
