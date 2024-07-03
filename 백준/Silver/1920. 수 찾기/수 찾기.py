import sys

def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            return True
    return False

nCount = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split(" ")))

mCount = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split(" ")))

nList.sort()

for m in mList:
    if binary_search(nList, m):
        print(1)
    else:
        print(0)
