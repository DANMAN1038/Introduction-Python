def rank_suit_count(cards):
    ranks = []
    suits = []
    for i in cards:
        for ele in range(0,2):
            if ele == 0:
                ranks.append(i[ele])
            else:
                suits.append(i[ele])
    rank_list = {}
    suit_list = {}
    for ele in ranks:
        count_rank = ranks.count(ele)
        rank_list[ele] = count_rank
    for suit in suits:
        count_suits = suits.count(suit_list)
        suit_list[suit] = count_suits
    print(rank_list, suit_list)
rank_suit_count(['AS', 'AD', '2C', 'TH', 'TS'])
