#library
import sys, re, heapq
from math import (
sin, cos, radians, ceil, 
floor, sqrt, isqrt, pi, 
gcd, comb, factorial
)
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def

#main
def main():
    N = int(input())
    S = list(input())
    
    for i, char in enumerate(S):
        if char == '1':
            if i % 2 == 0:
                print('Takahashi')
                exit()
            else:
                print('Aoki')
                exit()

    

if __name__ == '__main__':
    main()