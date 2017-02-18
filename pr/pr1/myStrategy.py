def myStrategy(myscore, theirscore, last):
    # diff := the difference between 100 and myscore
    diff = 100 - myscore

    # thresh1/2/3 := threshholds of point values at which the strategy will change tactics; mainly for sake of testing.
    thresh1 = 60
    thresh2 = 89
    thresh3 = 96

    # below is the output of the dict compt with some augmented values
    range_dict = {1: [range(0, 6), range(0, 8)],
                  2: [range(1, 9), range(0, 13)],
                  3: [range(2, 13), range(0, 17)],
                  4: [range(4, 16), range(0, 21)],
                  5: [range(6, 19), range(0, 25)],
                  6: [range(8, 22), range(1, 29)],
                  7: [range(10, 25), range(3, 32)],
                  8: [range(12, 28), range(4, 36)],
                  9: [range(14, 31), range(6, 39)],
                  10: [range(16, 34), range(7, 43)],
                  11: [range(18, 37), range(9, 46)],
                  12: [range(20, 40), range(11, 49)],
                  13: [range(22, 43), range(13, 52)],
                  14: [range(24, 46), range(14, 56)]
                  }

    # returns the aggressive and safe dice rolls for the given diff, as stored in the dict
    def range_dict_sort(diff=diff, dict=range_dict):
        empty = lambda ls: True if len(ls) == 0 else False
        aggr = []
        safe = []
        for i in dict:
            if diff in dict[i][0]:
                aggr.append(i)
            elif diff in dict[i][1]:
                safe.append(i)
        return [x[0] for x in (aggr, safe) if not empty(x)]


    # below_threshx := the sub-function to be used when myscore <= threshx
    def below_thresh1(myscore, theirscore, last):
        return diff // 3

    def below_thresh2(myscore, theirscore, last):
        if myscore < theirscore:
            return range_dict_sort()[0]
        elif myscore >= theirscore:
            return range_dict_sort()[1]

    def below_thresh3(myscore, theirscore, last):
        return (diff // 6) + 1

    def above_thresh3(myscore, theirscore, last):
        if myscore >= theirscore:
            return 0
        if myscore < theirscore:
            return 1

    # the basic control flow of the strategy:
    if myscore <= thresh1:
        return below_thresh1(myscore, theirscore, last)
    elif thresh1 < myscore <= thresh2:
        return below_thresh2(myscore, theirscore, last)
    elif thresh2 < myscore <= thresh3:
        return below_thresh3(myscore, theirscore, last)
    elif thresh3 < myscore:
        return above_thresh3(myscore, theirscore, last)
    else:
        return 0