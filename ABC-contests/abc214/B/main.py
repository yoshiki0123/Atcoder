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
    S, T = map(int,input().split())

    ans = 0
    for a in range(101):
        for b in range(101):
            for c in range(101):
                if a+b+c <= S and a*b*c <= T:
                    ans += 1
    
    print(ans)

    

if __name__ == '__main__':
    main()