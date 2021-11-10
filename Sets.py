def average(array):
    # your code goes here
    # y = 0
    # for x in array:
    #     y += x
    return sum(set(array)) / len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
