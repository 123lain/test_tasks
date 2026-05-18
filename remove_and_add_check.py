arr = [8, 1, 3, 16, -1, 4, 5]
n = 7
k = 6

def remove_and_add_check(arr: list[int], n: int, k: int) -> int:
    for i in range(k - 1, n - 1):
        if arr[i] != arr[i + 1]:    # check if all the elements starting from index k - 1 are equal.
            return -1               # if not, then it's impossible to get the desired array.

    for i in range(k - 2, -1, -1):  # we go in reverse order from k - 1
        if arr[i] != arr[k - 1]:    # we need to find the index of the last element that is not equal to arr[k-1]
            return i + 1            # that index + 1 will be the required amount of steps to get the desired array.

    return 0

if __name__ == '__main__':
    print(arr)
    print(remove_and_add_check(arr, n, k))