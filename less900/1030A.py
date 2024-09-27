# https://codeforces.com/problemset/problem/1030/A

EASY = "EASY"
HARD = "HARD"
output = EASY

n = input()
input_list = list(map(int, input().split()))

for i in input_list:
    if i == 0:
        continue
    else:
        output = HARD
        break

print(output)
