arr = [43, 54, 232, 13, 66, 1334, 313, 35]


def find_min_two_sum(arr: list[int]) -> (int, int):
    min_1 = float('inf')
    min_2 = float('inf')

    for i in arr:
        if i < min_1:
            min_2 = min_1
            min_1 = i
        elif i < min_2:
            min_2 = i
    return min_1, min_2


if __name__ == '__main__':
    print(arr)
    print(find_min_two_sum(arr))
