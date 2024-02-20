def SelectionSort(a):
    n=len(a)
    for i in range(n-2):
        min=i
        for j in range(i+1,n-1):
            if a[j]<a[min]:
                min=j
                temp=a[i]
                a[i]=a[min]
                a[min]=temp

        

a=[20,50,30,10,40]
print("Original Array",a)
SelectionSort(a)
print("Sorted Array",a)