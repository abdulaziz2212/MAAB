def list_none(arr):
    for i in range(1,len(arr)):
        if arr[i] == None:
            arr[i] = arr[i-1]
    print(arr)

list_none([None,1,2,3,None,4,None,None])


        