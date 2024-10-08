# https://codeforces.com/problemset/problem/136/A

if __name__ == '__main__':
    # num of friends
    n: int = int(input())

    gifts = list(map(int, input().split()))

    # [0, 0, 0, .. 0] # len = n
    receives = [0] * n

    for idx, g in zip(range(n), gifts):
        receives[g - 1] = idx + 1

    print(" ".join(str(_) for _ in receives))
