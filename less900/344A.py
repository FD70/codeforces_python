# https://codeforces.com/problemset/problem/344/A

num_of_islands = 1

if __name__ == '__main__':
    # count of magnets # 1 <= n <= 100_000
    n: int = int(input())

    tail: bool = bool(int(input()[-1]))
    for i in range(n - 1):
        _next: str = input()
        if tail == bool(int(_next[-1])):
            continue
        else:
            tail = not tail
            num_of_islands += 1

    print(num_of_islands)
