array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

def parent(i):
    return (i - 1) // 2

def left_child(i):
    return (i * 2) + 1

def right_child(i):
    return (i * 2) + 2

def maxHeapify(A, i, heapSize):
    left = left_child(i)
    right = right_child(i)
    largest = i
    if left <= heapSize and A[left] > A[i]:
        largest = left
    if right <= heapSize and A[right] > A[largest]:
        largest = right
    if largest != i:
        largestValue = A[largest]
        A[largest] = A[i]
        A[i] = largestValue
        maxHeapify(A, largest, heapSize)

def buildMaxHeap(A):
    heapSize = len(A) - 1
    lastParent = (len(A) - 1) // 2
    for i in range(lastParent, -1, -1):
        maxHeapify(A, i, heapSize)

def heapSort(A):
    buildMaxHeap(A)
    heapSize = len(A) - 1
    for i in range(heapSize, 0, -1):
        largestValue = A[0]
        A[0] = A[i]
        A[i] = largestValue
        heapSize -= 1
        maxHeapify(A, 0, heapSize)

print(array)

heapSort(array)

print(array)
