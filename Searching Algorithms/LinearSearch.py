#What is linear or Sequential search:
#It is a searching method that scans the list one by one from left to right or vice-versa
#If the element is found it returns the index, otherwise it returns -1(sentinel value)
#Complexity O(N), where N is the length of the list


def linearSearch(l,k):
  for i in range(len(l)):
    if k == l[i]:
      return i
  return -1

list1 = [6,15,3,97,24,16]
searched_value = int(input("Enter a value to search for: "))
print(linearSearch(list1,searched_value))
