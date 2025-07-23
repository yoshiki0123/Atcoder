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
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()

    s = {S1, S2, S3, S4}
    
    if len(s) == 4:
        print('Yes')
    else:
        print('No')

    
    

if __name__ == '__main__':
    main()