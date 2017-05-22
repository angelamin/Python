# -*- coding:UTF-8 -*-
#
# 算法概要：
# 给i, 提前将i的值保存在key中，j= i-1，j不断减小如果j比i大，那么j就后移一位，a[j+1] = a[j]，直到腾出一个位置，此时i的值比j小，这个位置就是该插入i的位置，进行插入


def insertSort(a):
    for i in range(1, len(a)): #范围最后是1，2，3，4  最后一个是没取到
        j = i -1
        key = a[i]
        while (j >= 0) and (a[j] > a[i]):
            a[j+1] = a[j]
            j = j - 1
        a[j + 1] = key # 此处之前j多减了1
    return a

if __name__ == '__main__':
    arr = [4, 2, 10, 6, 6]
    sorted = insertSort(arr)
    print sorted
