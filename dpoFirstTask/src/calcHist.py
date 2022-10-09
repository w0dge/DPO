def calcHist(tdata):
    #   hist is a List to store histogram. It contains [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    hist = [0] * 10
    for value in tdata:
    #   Calculate histogram for tdata List
        if value >= 900:
            hist[9] += 1
        elif value >= 800:
            hist[8] += 1
        elif value >= 700:
            hist[7] += 1
        elif value >= 600:
            hist[6] += 1
        elif value >= 500:
            hist[5] += 1
        elif value >= 400:
            hist[4] += 1
        elif value >= 300:
            hist[3] += 1
        elif value >= 200:
            hist[2] += 1
        elif value >= 100:
            hist[1] += 1
        elif value >= 0:
            hist[0] += 1

    return hist


# Next fragment is for test

#   data contains List with size 1000 000 with 0 values
#
# data = [0] * 1000000
#
# a = calcHist(data)
#
# print(a)
