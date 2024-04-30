def Merge(A, s, m, e):
    n1 = m - s + 1
    n2 = e - m
    L = []
    R = []
    for i in range(0 , n1):
        L.append(A[s + i])
    for j in range(0, n2):
        R.append(A[m + 1 + j])

    i = 0
    j = 0
    k = s

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1

    while i < n1:
        A[k] = L[i]
        i = i + 1
        k = k + 1

    while j < n2:
        A[k] = R[j]
        j = j + 1
        k = k + 1

def Merge_Sort(A, s, e):
    if s < e:
        m = (s + e) // 2
        Merge_Sort(A, s, m)
        Merge_Sort(A, m + 1, e)
        Merge(A, s, m, e)

array = [5, 3, 2, 1, 4]

print(array)

e = len(array) - 1

Merge_Sort(array, 0, e)

print(array)
