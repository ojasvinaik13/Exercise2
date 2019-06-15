def bubble_sort(a, n):
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


n = int(input("Enter the number of elements in the array:"))
a = []
print("Enter the elements of the array:")
for i in range(n):
    num = int(input())
    a.append(num)

bubble_sort(a, n)

print("The array after sorting in ascending order using bubble sort algorithm is:")
for i in range(n):
    print(a[i])
