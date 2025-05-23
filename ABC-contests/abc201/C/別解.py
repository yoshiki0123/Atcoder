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
    S = input()
    N = 4
    ans = 0
    for i in range(10 ** N):
        flag = ['x' for j in range(10)]
        for d in '{:0{}}'.format(i, N):
            flag[ord(d) - ord('0')] = 'o'
        ans += all(S[j] == '?' or S[j] == flag[j] for j in range(10))
    print(ans)

if __name__ == '__main__':
    main()