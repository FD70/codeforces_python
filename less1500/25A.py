# https://codeforces.com/problemset/problem/25/A

even_count = 0
odd_count = 0


class Evenness:
    EVEN = 0
    ODD = 1


def find_first(remains, _list) -> int:

    for idx, number in zip(range(len(_list)), _list):
        if number % 2 == remains:
            return idx
    return -1


if __name__ == '__main__':
    n: int = int(input())

    input_array = list(map(int, input().split()))

    ans = 0
    # enough 3 numbers to indicate
    for i in range(3):
        if input_array[i] % 2 == 0:
            even_count += 1
            if even_count == 2:
                ans = find_first(Evenness.ODD, input_array)
                break
        else:
            odd_count += 1
            if odd_count == 2:
                ans = find_first(Evenness.EVEN, input_array)
                break

    print(ans + 1)
