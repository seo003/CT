import sys

count = int(sys.stdin.readline())
nums = []

for _ in range(count):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for num in nums:
    print(num)