inp = input("Enter the number : ").split(" ")
arr = [int(v) for v in inp]

print("Before sorted : ",[x for x in arr])

def partition(arr,low,high):
    p = arr[low]
    i = low+1
    j = high
    while True:
        while i<=j and arr[i]<=p:
            i=i+1
        while i<=j and arr[j]>=p:
            j=j-1
        if i<=j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
        
    arr[low],arr[j] = arr[j],arr[low]
    return j
            
    
def quick_sort(array,low,high):
    if low < high :
        pivot = partition(array,low,high)
        #calling the same function for 
        quick_sort(array,low,pivot-1)
        quick_sort(array,pivot+1,high)
        

quick_sort(arr,0,(len(arr)-1))

print("After sorting : ",[v for v in arr])