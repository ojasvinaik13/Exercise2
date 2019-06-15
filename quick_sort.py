def partition(a, s, e):
    pivot = a[e]
    start = s-1
    for i in range(s, e):
        if a[i] < pivot:
            start = start + 1
            a[start], a[i] = a[i], a[start]

    a[start+1], a[e] = a[e], a[start+1]

    return start+1


def quick_sort(a, s, e):
    if s < e:
        index = partition(a, s, e)
        quick_sort(a, s, index-1)
        quick_sort(a, index+1, e)


n = int(input("Enter the number of elements in the array:"))
arr = []
print("Enter the elements of the array:")
for i in range(n):
    num = int(input())
    arr.append(num)

quick_sort(arr, 0, n-1)

print("The array after sorting in ascending order using quick sort algorithm is:")
for i in range(n):
    print(arr[i])
