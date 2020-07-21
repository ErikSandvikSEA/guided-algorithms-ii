# partition function handles the work of selecting a pivot element
# and partitioning the data in the array around the pivot
# going to return the left partition, the pivot, and the right partition
def partition(arr):
    # pick the first element as the pivot element
    pivot = arr[0]
    left = []
    right = []

    # iterate through the rest of the array, putting each element in the appropriate bucket
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return left, pivot, right


def quicksort(arr):
    # base case
    # if the length of the array is 0
    if len(arr) <= 1:
        return arr

    # how do we get closer to our base case?
    left, pivot, right = partition(arr)

    return quicksort(left) + [pivot] + quicksort(right)


arr = [2, 6, 7, 4, 2, 77, 87, -44444, 54, 3]

print(quicksort(arr))
