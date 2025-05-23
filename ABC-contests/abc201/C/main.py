#library
import sys, re, heapq
from math import sin, cos, radians, ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def

#main
def main():
    S = list(input())
    ans = 0

    for i in range(10000):
        num_list = list(str(i).zfill(4))
        tmp_S = ['x']*10

        for j in num_list:
            j = int(j)
            tmp_S[j] = 'o'
    
        flg = True
        for k in range(10):
            if S[k] == 'o' and tmp_S[k] != 'o':
                flg = False
                break
            
            if S[k] == 'x' and tmp_S[k] != 'x':
                flg = False
                break
            
        if flg:
                ans += 1
        
    print(ans)

if __name__ == '__main__':
    main()