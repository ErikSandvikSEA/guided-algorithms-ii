def bubble_sort(arr):
    swaps_occurred = True
    # iterating through the arr and looking at elements two at a time
    # swapping them if they're out of order
    while swaps_occurred:
        # toggle the boolean
        swaps_occurred = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # swap!
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps_occurred = True

    return arr
    # if we do this all the way through, all the elements will eventually end up in sorted order
    # we know all the elements are in sorted order when no swaps occur
    # parallel to selection sort: builds up the sorted portion of the array starting by putting the largest element at the end

    # the number of iterations through the array that we need to make is equal to the number of elements in the array  - O(n^2)


def recursive_bubble_sort(arr, unsorted_length):
    # base case(s)
    # re-use the swaps_occurred boolean idea
    # the boolean tells us when the unsorted portion reaches 0
    # if the length of the unsorted portion is 0
    if unsorted_length > 0:
        recursive_bubble_sort(arr, unsorted_length - 1)
    # how do we get closer to the base case?
    # each pass shortens the unsorted portion by 1
    # each pass does the same exact thing as what it does in the iterative implementation
    for i in range(unsorted_length - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

