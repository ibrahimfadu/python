def LeanearSearch(arr,key):
    n=len(arr)
    for i in range (0,n):
        if key==arr[i]:
            return i
    return -1
arr=[12,34,76,45,32,43,64,93,61,60,20]
key=93
result=LeanearSearch(arr,key)
if result==-1:
    print("Elemet is not present ")
else :
    print("Element is present ")
