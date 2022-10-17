import os.path


def triangle(amountOfStarsAroundMiddle):
    amountOfStars = 1
    amountOfSpaces = amountOfStarsAroundMiddle
    histForType = list()
    histForCount = list()
    while amountOfStars <= (amountOfStarsAroundMiddle * 2 + 1):
        stars = " " * amountOfSpaces + "*" * amountOfStars
        histForType.append(stars)
        histForCount.append(amountOfStars)
        amountOfStars += 2
        amountOfSpaces -= 1
        print(stars)
    return [histForType, histForCount]


# В path передается имя файла
def writeHistToFile(path, amountOfStars):
    file = open(path + '.txt', 'w')
    hist = triangle(amountOfStars)[0]
    for row in hist:
        file.write(row + '\n')
    file.close()


# В  path передается имя файла (подразумевается, что он лежит в той же директории, где и исполняемый файл)
def readHistFromfile(path):
    path += '.txt'
    if os.path.exists(path):
        file = open(path)
        notFormattedHist = file.read()
        formattedHist = list(filter(None, notFormattedHist.split('\n')))
        numericHist = toNumeric(formattedHist)
        return numericHist
    return 'Wrong name of file, or it does not exists'


def histDistance(hist1, hist2) -> float:
    distance = 0
    for index in range(len(hist1)):
        distance += (hist1[index] - hist2[index]) ** 2

    return distance ** 0.5


def toNumeric(hist):
    sideLen = len(hist[-1])
    newHist = [0] * sideLen
    for n in hist:
        for index in range(sideLen):
            if (index < len(n)) and (n[index] != ' '):
                newHist[index] += 1
    return newHist


# print('Введите пути файлов с гистаграммами одинаковой размерности, либо, если хотите использовать уже имеющиеся в проекте файлы для тестирования, оставьте имена пустыми\n')
# path1 = input('Путь до hist1 (без расширения): ')
# path2 = input('Путь до hist2 (без расширения): ')
#
# if not path1:
#     path1 = 'hist'
# if not path2:
#     path2 = 'hist2'

# print('Расстояние между гистаграммами содержащимися в файлах', path1,
#       'и', path2, '=', histDistance(readHistFromfile(path1), readHistFromfile(path2)))

print('Расстояние между гистаграммами из файлов:', histDistance(readHistFromfile('hist1'), readHistFromfile('hist2')))
