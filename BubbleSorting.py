def BubbleSort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
a=[30,10,20,50,40]
print("Original array",a)
BubbleSort(a)
print("Sorted array",a)
