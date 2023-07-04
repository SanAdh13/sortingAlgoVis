import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


sample = [random.randint(1,1000_0) for _ in range(300)] 
fig,ax = plt.subplots()

def final(bars,arr):
    # Final visualization
    for i in range(len(arr)):
        bars[i].set_color('black')

    plt.pause(0.5)
    plt.show()

def currComparison(bars,arr,firstIndex,secondIndex):
    bars[firstIndex].set_height(arr[firstIndex])
    bars[secondIndex].set_height(arr[secondIndex])
    bars[firstIndex].set_color('g')  
    bars[secondIndex].set_color('r')  
    # Pause for a short while to visualize the changes
    plt.pause(0.005)

    # Reset the color of previous comparisons to red
    bars[firstIndex].set_color('b')
    bars[secondIndex].set_color('b')

def bubblesort(arr):
    '''
    Bubble sort works by traversing through the array and comparing & swapping neighbours 
    till sorted
    '''
    ax.set_title('Bubble Sort')    

    bars  = ax.bar(range(len(arr)),arr)
    for x in range(len(arr)-1):
        for j in range(len(arr)-x-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

            currComparison(bars,arr,j,j+1)


    final(bars,arr)


def selection(arr):
    '''
    Selection sort works by selecting the first index and traversing through the entire array
    After traversing the entire array 
        the lowest value is found and the current index and index of lowest number swapped
    '''
    ax.set_title('Selection Sort')    

    bars = ax.bar(range(len(arr)),arr)
    for x in range(len(arr)-1):
        lowestNIndex = x

        for y in range(x+1,len(arr)):
            if arr[y] < arr[lowestNIndex]:  
                lowestNIndex = y
        if lowestNIndex != x:
            arr[x],arr[lowestNIndex] = arr[lowestNIndex],arr[x]  

            currComparison(bars,arr,x,lowestNIndex)


    final(bars,arr)

def insertionSort(arr):
    ''' 
    Insertion sort works by comparing the values to the left of it; starting from second element
    values moved repeatdly to the left until it meets a smaller number
    moves to the next item in the list when smaller number met
    '''
    ax.set_title('Insertion Sort')    

    bars  = ax.bar(range(len(arr)),arr)
    for i in range(1,len(arr)):
        temp,pos = arr[i] , i-1

        while pos >= 0 and arr[pos] > temp:
                arr[pos+1] = arr[pos]
                currComparison(bars,arr,pos+1,pos)

                pos-=1

        
        arr[pos+1] = temp
        # same index twice lol
        currComparison(bars,arr,pos+1,pos+1)

        plt.pause(0.05)

    final(bars,arr)
    

def quicksort(arr):
    '''
    Quicksort is a recursive algo, the last element is used as pivot 
    partition made where smaller and larger numbers are to either side of the pivot
    for each partition, the pivot and partitioning is done till sorting is done
    '''
    ax.set_title('QuickSort')    

    bars = ax.bar(range(len(arr)),arr)

    # from 'A common sense guide to Data-Structures' ruby code adapted into python lol 
    def partition(arr,low,high):
        pivotIndex = high
        pivotVal = arr[pivotIndex]
        high-= 1

        
        while True:
            while arr[low] < pivotVal:
                low+=1
            
            while arr[high] > pivotVal:
                high-=1
            
            if low >= high:
                break
            else:
                arr[low],arr[high]=arr[high],arr[low]

                currComparison(bars,arr,low,high)
                low+=1
                        
        arr[low],arr[pivotIndex] = arr[pivotIndex],arr[low]
        currComparison(bars,arr,low,pivotIndex)
        return low
    
    def qSort(arr,low,high):
        if low<high:
            pivotIndex = partition(arr,low,high)
            qSort(arr,low,pivotIndex-1)
            qSort(arr,pivotIndex+1,high)

    qSort(arr,0,len(arr)-1)    
    final(bars,arr)



if __name__ == "__main__":
    bubblesort(sample.copy())
    selection(sample.copy())
    insertionSort(sample.copy())
    quicksort(sample.copy())



