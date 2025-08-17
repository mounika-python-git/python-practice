
    def getSecondLargest(self, arr):
        arr.sort()
        k=arr[-1]
        m=-1
        for i in range(len(arr)-2,-1,-1):
            
            if arr[i]!=k:
                m=arr[i]
                break
            
        return m
    arr=int(input())
    print(getSecondLargest(arr))
        

