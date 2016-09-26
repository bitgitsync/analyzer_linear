#! /usr/bin/env python

import itertools
import numpy 

def countSameSum (listName):
    
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = [[]]
    countHowManypossibleResult = 0
#    howManyPossibleResult = 0

    list1 = listName
#    print('Input is ', sorted(list1))

    for i in range(1, len(list1)):
        list3 = sorted(list(itertools.combinations(list1, i)))
        list2 = [[0] for j in range(0,len(list3[i - 1]))]
        for m in range (0, len(list3)):
            for k in range (0, len(list3[i - 1])):
                list2[k] = list3[m][k]
            list4 = sorted(list(set(list1).difference(set(list2))))
            list5 = sorted(list2)
            if (numpy.sum(list5) == numpy.sum(list4)):
                list6 += ([[list5 ] + [list4 ] ])
                countHowManypossibleResult += 1

    if countHowManypossibleResult == 0 :
        print('No Possible to separe into two group have same sum')

    list6 += [countHowManypossibleResult]
    return  list6       

if __name__ == '__main__':

    theResultListName = [[]]
    listNeedToCount = [5, 9, 7, 11, 14, 13, 22, 24, 25]

    theResultListName = countSameSum (listNeedToCount)
    for howManyPossibleResult in range(1, theResultListName[-1]) :
        
        print(theResultListName[howManyPossibleResult][0], theResultListName[howManyPossibleResult][1])

