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
    P = int(input())
    ans = 0
    for i in range(10, 0, -1):
        sub = factorial(i)

        while P >= sub:
            P -= sub
            ans += 1
    
    print(ans) 

if __name__ == '__main__':
    main()