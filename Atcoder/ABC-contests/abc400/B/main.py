#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#def


#main
def main():
    N, M = map(int,input().split())
    
    X = 0
    for i in range(M + 1):
        X += N ** i
    
    if X <= 10 ** 9:
        print(X)
    else:
        print('inf')


    

if __name__ == '__main__':
    main()

