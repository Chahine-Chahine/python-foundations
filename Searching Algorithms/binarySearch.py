#Binary search:
#Works only on sorted lists
#It repeatedlly divide the list into half, comparing the middle element with the largest value until the element is found or the sublist size become 1.
#Complexity O(lg N), where n is the length of the list

def binarySearch(l,k):
  low = 0
  high = len(l) - 1
  while low <= high:
    mid = (low+high) // 2
    if k == l[mid]:
      return mid
    elif k < l[mid]:
      high = mid - 1
    elif k > l[mid]:
      low = mid + 1

list2 = [x for x in range(1,100)]
searched_for =  int(input("Enter a value to search for: "))
print(binarySearch(list2,searched_for))