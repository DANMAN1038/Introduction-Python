def make_dictionary(names, scores):
    score_dict = {}
    for i in range(0, len(names)):
        score_dict[names[i]] = scores[i]
    print(score_dict["barb"])
    score_dict["John"] = 19
    total = 0
    for ele in scores:
        total += ele
    average = total / len(names)
    print(average)
    del score_dict["harry"]
    score_dict["Sally"] = 13
def get_score(name, dictionary):
    if name in dictionary:
        print(score_dict[name])
    else:
        return -1
make_dictionary(['joe', 'harry', 'barb', 'sue', 'sally'], [10,23,13,18,12])
