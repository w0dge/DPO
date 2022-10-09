import time
import millionArray
import calcHist


def determineTheTime(data):
    start = time.time()

    calcHist.calcHist(data)

    end = time.time()

    return end - start


array = millionArray.initListWithRandomNumbers()

print('Длительность работы программы calcHist =', determineTheTime(array))

timeList = [];
for i in range(100):
    timeList.append(determineTheTime(array))

print('Минимальное время работы программы calcHist = ', min(timeList))
print('Максимальное время работы программы calcHist = ', max(timeList))
print('Средняя время работы программы calcHist = ', sum(timeList)/len(timeList))
