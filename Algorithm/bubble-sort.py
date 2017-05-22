# -*- coding:utf-8 -*-
# 从数组开头开始，比较一对数，大的放在后一个，一直比较到数组末尾，
# 此时，数组最后一个数是最大的，
# 之后便比较对数除去最后一个数，因为已经将它最大了，不用再比较
def bubble(arr):
    arrLen = len(arr) # 用来记录比较的总个数
    while arrLen > 0:
        for i in range(arrLen - 1):
            j = i + 1
            if arr[i] > arr[j]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
        arrLen = arrLen - 1
    return arr

if __name__ == '__main__':
    arr = [4,6,34,0,0]
    array = bubble(arr)
    print array