# 解决N皇后问题
# 设计 皇后会攻击横排,竖排,斜排,在NxN的牌局中,摆放N个皇后,有几个解法?
import sys

import time
from matplotlib import pyplot

LATTICE_COUNT = 3


# QUEENS = []


#
# def can_add(read_queen,pos):
#     for queen in read_queen:
#         #判断该位置是不是符合要求?
#
# def put_other(first_index):
#     r, c = 0, 0
#     queen_count = 8 - 1  # 剩下7个皇后
#     queen = []
#     queen.append(first_index)
#     while queen_count > 0:
#         while r < LATTICE_COUNT:
#             while c < LATTICE_COUNT:
#                 #这里判断是否合格
#                 c += 1
#             r += 1
#
# sys.setrecursionlimit(1000000)
# sys.setrecursionlimit(1500000)

#
# def in_queen_eat(queen, pos_c, pos_r):
#     for (c, r) in queen:
#         if c == pos_c or r == pos_r or c - pos_c == r - pos_r:
#             return False
#     return True
#
#
# def insert(queen, pos_c, pos_r, cur_depth):
#     print('is:' + str(cur_depth))
#     old_queen = queen[:]
#     cache_queen = queen[:]
#     can_add = in_queen_eat(cache_queen, pos_c, pos_r)
#
#     if can_add:
#         # 加上.为一个解
#         cache_queen.append((pos_c, pos_r))
#         next_r = pos_r + 1
#         if next_r < LATTICE_COUNT:
#             print('go next:' + str(pos_c) + '  r:' + str(next_r) + ' cache_queen:' + str(cache_queen))
#             insert(old_queen, pos_c, next_r, cur_depth + 1)
#             # 这里要找这一排下一个的解法
#
#     pos_r += 1
#     if pos_r >= LATTICE_COUNT:
#         pos_c += 1
#         pos_r = 0
#     if pos_c < LATTICE_COUNT:
#         insert(cache_queen, pos_r, pos_c, cur_depth + 1)
#     else:
#         if len(cache_queen) == LATTICE_COUNT:
#             QUEENS.append(cache_queen)
#
#
# def prepare():
#     queen = []
#     insert(queen, 0, 0, 1)
#     print(QUEENS)

# first_index = (0, 0)


# prepare()
# 原始
def queen(QUEENS, A, cur=0):
    if cur == len(A):
        QUEENS.append(A[:])
        # print(A)
    else:
        # A = [None] * 8
        for col in range(len(A)):
            A[cur] = col  # 表示把第cur行的皇后放在col列上
            ok = True
            for r in range(cur):
                if A[r] == col or r - A[r] == cur - A[cur] or r + A[r] == cur + A[cur]:  # 判断是否跟前面的皇后冲突
                    ok = False
                    break
            if ok:
                queen(QUEENS, A, cur + 1)


#
A = [None] * 13
QUEENS = []
start = time.time()

queen(QUEENS, A)
end = time.time()
print(end - start)
# for arr in QUEENS:
#     print(arr)


# 自己写的,竟然快我1倍左右.
def queen2(QUEENS2, arr, rol=0):
    if rol == len(arr):
        QUEENS2.append(arr[:])
        # print(arr)
        return
    # print(rol)
    for col in range(len(arr)):
        arr[rol] = col
        ok = True
        for r in range(rol):
            if arr[r] == col or abs(col - arr[r]) == abs(rol - r):
                ok = False
        if ok:
            queen2(QUEENS2, arr, rol + 1)


QUEENS2 = []

# start = time.time()
# queen2(QUEENS2, A)
# end = time.time()
# print(end - start)
# print(len(QUEENS2))
# for arr in QUEENS2:
#     print(arr)
# c = []
# b = set( QUEENS2 )
# for i in QUEENS:
#     if i not in b:
#         c.append( i )
#
# print(c)
# print(set(QUEENS2) ^ set(QUEENS))

# from pylab import *
#
# np.po
# X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
# C,S = np.cos(X), np.sin(X)
#
# pyplot.plot(X,C)
# pyplot.plot(X,S)
# pyplot.show()
