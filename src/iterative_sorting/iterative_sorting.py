# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # Swapping positions
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # temp = arr[cur_index]
        # arr[cur_index] = arr[smallest_index]
        # arr[smallest_index] = temp
    

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(len(arr)):
        
        for j in range(len(arr) - (i - 1)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    if not arr:
        return []
    if min(arr) < 0:
        print("Negative numbers not allowed")
        return None
    result = []
    temp_bucket = [0 for _ in range(max(arr) + 1)]
    for x in arr:
        temp_bucket[x] += 1
    for i in range(len(temp_bucket)):
        while temp_bucket[i] > 0:
            result.append(i)
            temp_bucket[i] -= 1

    return arr
