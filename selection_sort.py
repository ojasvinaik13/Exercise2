def selection_sort(a, n):
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


n = int(input("Enter the number of elements in the array:"))
a = []
print("Enter the elements of the array:")
for i in range(n):
    num = int(input())
    a.append(num)

selection_sort(a, n)

print("The array after sorting in ascending order using selection sort algorithm is:")
for i in range(n):
    print(a[i])
