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
    N = int(input())
    P = [0] + list(map(int, input().split(' ')))

    ans = 0
    sign = []

    for right in range(2, N+1):
        if P[right - 1] < P[right]:
            sign.append('+')
            
        if P[right - 1] > P[right]:
            sign.append('-')
    
    sign_list = []
    len_list = []
    current = sign[0]
    count = 1
    for s in sign[1:]:
        if s == current:
            count += 1
        else:
            sign_list.append(current)
            len_list.append(count)
            current = s
            count = 1
    sign_list.append(current)
    len_list.append(count)

    ans = 0
    for i in range(len(sign_list) - 2):
        if sign_list[i] == '+' and sign_list[i+1] == '-' and sign_list[i+2] == '+':
            ans += len_list[i] * len_list[i+2]

    print(ans)   

 


if __name__ == '__main__':
    main()