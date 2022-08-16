def remove_punc(text, punc):
    for ele in text:
        if ele == punc:
            replacement = text.replace(punc,'')
            return(replacement)
print(remove_punc('Rem!ove, o?nly th3 exc!amati.n points!', '!'))
