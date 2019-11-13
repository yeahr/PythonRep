import math
import random
'''
author: yeahr
this line is deleting
'''

def subSet(setA, setB):
    begin = max(setA[0],setB[0])
    end = min(setA[1],setB[1])
    if begin <= end:
        return [begin,end]
    else:
        return [0,0]

def randSet():
    begin = random.randrange(0,10000)
    end = random.randrange(begin,10000)
    ll = [begin,end]
    print(ll)
    return ll

def main():
    seta = randSet()
    setb = randSet()
    print(subSet(seta,setb))

if __name__ == "__main__":
    main()
