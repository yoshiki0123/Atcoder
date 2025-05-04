#library
import sys, re
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#def

#main
def main():
    T = list(input())
    U = list(input())
    
    for i in range(len(T) - len(U)+1):
        can_flg = True
        S = T[i:i+len(U)]

        for j, e in enumerate(S):
            if e != U[j] and e != '?':
                can_flg = False
                break 
        
        if can_flg:
            print('Yes')
            exit() 

    print('No')  
    

    
    

if __name__ == '__main__':
    main()