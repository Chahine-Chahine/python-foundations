#Selection Sort:
#Starts by finding the smallest element in the list and swaps it with the element at index 0
#Then it finds the next smallest number in the list and swaps it with the element at index 1
#This proccess continues until the list is sorted
#It involves two nested loops, where the first loop goes through the entire list and the second loop checks for the minimum value each time.
# Complexity: worst case O(N^2), where N is the length of the list


def selectionSort(l):
    for i in range(len(l) - 1):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                l[i] , l[j] = l[j] , l[i]
    return l

list1 = [16,8,19,23,34,14,6,56]
print(selectionSort(list1))
