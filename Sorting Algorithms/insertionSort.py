#InsertionSort:
#Sorting Algorithm that compares each element with the one before it and swaps if needed until the list is sorted
# Complexity: worst case O(N^2), where N is the length of the list 


list1 = [16,10,8,12,64,35,7,4,15,88]

def insertionSort(l):
    for i in range(1,len(l)):
        current = l[i]
        j = i - 1
        while j >= 0 and current < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = current
    print(f"The sorted list is {l}")
    

print(insertionSort(list1))