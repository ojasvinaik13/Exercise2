def insertion_sort(a, n):
    for i in range(1, n):
        e = a[i]
        j = i-1
        while j >= 0:
            if e < a[j]:
                a[j+1] = a[j]
                a[j] = e
            j = j-1
    

n = int(input("Enter the number of elements in the array:"))
a = []
print("Enter the elements of the array:")
for i in range(n):
    num = int(input())
    a.append(num)

insertion_sort(a, n)

print("The array after sorting in ascending order using insertion sort algorithm is:")
for i in range(n):
    print(a[i])
