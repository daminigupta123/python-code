A, B = map(int, input().split())
lucky_nums = []
for num in range(A, B + 1):
    s = str(num)
    if all(ch in '47' for ch in s):
        lucky_nums.append(num)
if lucky_nums:
    print(*lucky_nums)
else:
    print(-1)
# This code finds and prints all "lucky numbers" (numbers consisting only of digits 4 and 7) within a given range [A, B]. If no lucky numbers are found, it prints -1.
