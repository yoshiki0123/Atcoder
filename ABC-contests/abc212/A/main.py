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
    A, B = map(int,input().split())

    if 0 < A and B == 0:
        print('Gold')
    elif A == 0 and 0 < B:
        print('Silver')
    else:
        print('Alloy')
    
    

if __name__ == '__main__':
    main()