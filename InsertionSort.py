def InsertionSort(a):
    n=len(a)
    for i in range(1,n-1):
        k=a[i]
        j=i-1
        while j>=0 and a[j]>k:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=k
x=[40,20,30,10,50]
print("Origial array",x)
InsertionSort(x)
print("Sorted Array",x)
