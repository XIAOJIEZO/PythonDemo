#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 23:00
# @Author  : XIAOJIEZI

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    arr = [32, 54, 65, 32, 23, 87, 9]
    print(bubble_sort(arr))
