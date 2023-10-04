#Bubble Sort:
#Is the simplest sorting algorithm that works by repeatedlly swapping adjacent elements if they are not in the correct order
#The list is considered sorted when an iteration is ccompleted without any swaps
# An optimization using -i helps improve runtime
#Complexity: worst case O(N^2), Where N is the length of the list



list1 = [16,10,8,12,64,35,7,4,15,88]

def bubbleSort(l):
    for i in range(len(l)-1):
        for j in range(len(l)- i - 1):
            if l[j] > l[j+1]:
                l[j] , l[j+1] = l[j+1] , l[j]
    return l

print(bubbleSort(list1))