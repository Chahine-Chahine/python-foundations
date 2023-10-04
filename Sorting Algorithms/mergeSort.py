#Nearly the most efficient sorting algorithm 
#(Devide/conquer/merge)
#The process of dividing and merging continues until the list is sorted.
#Complexity: worst case O(N lg N), where N is the number of elements in a list 


def mergeSort(l):
    if len(l) > 1:
        mid = len(l) // 2
        sub_list1 = l[ : mid]
        sub_list2 = l[mid : ]
        mergeSort(sub_list1)
        mergeSort(sub_list2)
        i = j = k = 0
        while i < len(sub_list1) and j < len(sub_list2):
            if sub_list1[i] < sub_list2[j]:
                l[k] = sub_list1[i]
                i += 1
            else:
                l[k] = sub_list2[j]
                j += 1
            k += 1
        while i < len(sub_list1):
            l[k] = sub_list1[i]
            i += 1
            k +=1 
        while j < len(sub_list2):
            l[k] = sub_list2[j]
            j += 1
            k += 1
        return l

list1 = [16,10,8,12,64,35,7,4,15,88]

print(mergeSort(list1))