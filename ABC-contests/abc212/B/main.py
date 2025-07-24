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
    S = input()
    weak_s = S[0]
    tmp = S[0]
    for i in range(len(S)-1):
        tmp = int(tmp) + 1
        tmp = str(tmp)[-1]
        weak_s += tmp
    
    if S == weak_s or S[0] == S[1] == S[2] == S[3]:
        print('Weak')
    else: 
        print('Strong')

if __name__ == '__main__':
    main()