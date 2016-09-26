import itertools

def sorttwolist(l1):
    l4 = []
    l2 = sorted(l1)
    countHowManyResult = 0    
    for x in range (1, len(l2)):
        l4 += sorted(list(itertools.combinations(l2, x)))
    k = len(l4)
    for j in range (0, k//2):
        if sum(l4[j]) == sum(l4[k-j-1]):
            print(l4[j], l4[k-j-1])
            countHowManyResult += 1
    return countHowManyResult

if __name__ == '__main__':
    
    l1 = [1,2,3,4,5,6,7]
    if sorttwolist(l1) == 0 :
        print("No result.")

