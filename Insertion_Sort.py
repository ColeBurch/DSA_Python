def insertion_sort(A):
    for j in range(1, len(A)):
        current = A[j]
        i = j - 1
        while i >= 0 and A[i] > current:
            A[i + 1] = A[i]
            i = i -1
        A[i + 1] = current
    return(A)

test_1 = [5, 2, 4, 6, 1 , 3]
test_2 = [-1, 0, 1, 2]
test_3 = [1, -1, 2, 0]

print(insertion_sort(test_1))
print(insertion_sort(test_2))
print(insertion_sort(test_3))
