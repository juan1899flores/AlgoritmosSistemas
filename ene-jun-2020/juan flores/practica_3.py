def bub_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(arr[j]) > len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input())

arr = []
for i in range(n):
    arr.append(input())

bub_sort(arr)

print("\n"+"\n".join(arr))