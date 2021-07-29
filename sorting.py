import heapq

class Sorting:
    #Time Complexity  -> O(N^2)
    #Space Complexity -> O(1)
    def bubbleSort(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr

    #Time Complexity  -> O(N^2)
    #Space Complexity -> O(1)
    def selectionSort(self,arr):
        for i in range(len(arr)):
            minIndex = i
            for j in range(i+1,len(arr)):
                minIndex = j if arr[j]<arr[minIndex] else minIndex
            arr[i],arr[minIndex] = arr[minIndex],arr[i]
        return arr

    #Time Complexity  -> O(N^2)
    #Space Complexity -> O(1)
    def insertionSort(self,arr):
        for i in range(1,len(arr)):
            for index in range(i+1):
                if arr[index]>=arr[i]:
                    break
            temp = arr[i]
            for j in range(index,i+1):
                temp,arr[j] = arr[j],temp
        return arr

    #Time Complexity  -> O(N*Log(N))
    #Space Complexity -> O(N)
    def mergeSort(self,arr):
        if len(arr)==1:
            return arr
        
        mid = len(arr)//2

        left,right = self.mergeSort(arr[0:mid]),self.mergeSort(arr[mid:])

        mergedSubArr = []
        i1,i2 = 0,0

        while i1<len(left) and i2<len(right):
            if left[i1]<=right[i2]:
                mergedSubArr.append(left[i1])
                i1+=1
            else:
                mergedSubArr.append(right[i2])
                i2+=1
        
        for i in range(i1,len(left)):
            mergedSubArr.append(left[i])
        for i in range(i2,len(right)):
            mergedSubArr.append(right[i])
        
        return mergedSubArr
    
    #Time Complexity -> O(N*Log(N))
    #Space Complexity -> O(Log(N)) -> space taken in call Stack
    def quickSort(self,arr):
        return self._qucikSort(0,len(arr)-1,arr)

    def _qucikSort(self,start,end,arr):
        print(start,end)
        if start>=end:
            return

        boundary,i = start-1,start

        while i<end:
            if arr[i]<=arr[end]:
                arr[boundary+1],arr[i] = arr[i],arr[boundary+1]
                boundary+=1
            i+=1

        arr[boundary+1],arr[end] = arr[end],arr[boundary+1]

        self._qucikSort(start,boundary,arr)
        self._qucikSort(boundary+2,end,arr)

        return arr
    
    #Time Complexity -> O(N*Log(N))
    #Space Complexity -> O(N)
    def heapSort(self,arr):
        heap = []
        for i in arr:
            heapq.heappush(heap,i)
        arr = []
        while heap:
            arr.append(heapq.heappop(heap))

        return arr

    #Time Complexity -> O(N*L) where l is length of str() of max of array
    #space Complexity -> O(N)
    def radixSort(self,arr):
        sortedPositive = self._radixSort([i for i in arr if i>=0])
        sortedNegative = [-1*i for i in self._radixSort([-1*i for i in arr if i<0])[::-1]]

        return sortedNegative + sortedPositive

    def _radixSort(self,arr):
        if not arr:
            return arr
        queueArr = [[] for i in range(10)]
        repeat = len(str(max(arr)))

        arr = map(str,arr)

        for i in range(1,repeat+1):
            for j in arr:
                if i>len(j):
                    queueArr[0].append(j)
                else:
                    queueArr[int(j[-i])].append(j)
            arr = []
            for queue in queueArr:
                while queue:
                    arr.append(queue.pop(0))
        return [i for i in map(int,arr)]

    #Time Complexity -> O(N*Log(k)) Reduces N to k which corresponds to number of decks in patienceArr[]
    #Space Complexity -> O(N) 
    def patienceSort(self,arr):
        patienceArr = []
        for i in arr:
            found = False
            for j in patienceArr:
                if j[-1]>=i:
                    j.append(i)
                    found = True
                    break
            if not found:
                patienceArr.append([i])
        
        heap = []
        for i in range(len(patienceArr)):
            heapq.heappush(heap,[patienceArr[i][-1],i,len(patienceArr[i])-1])
        
        result = []
        while heap:
            el,row,col = heapq.heappop(heap)
            result.append(el)
            if col:
                heapq.heappush(heap,[patienceArr[row][col-1],row,col-1])
        return result