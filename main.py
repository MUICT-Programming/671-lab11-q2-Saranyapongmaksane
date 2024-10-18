# YOUR CODE HERE
n =int(input())
list1 = []
list2 = []

for i in range(n):
    list1.append(int(input()))
for i in range(n):
    list2.append(int(input()))

def summation(lst1,lst2):
    updated_list =[]
    for i in range(n):
        updated_list.append(lst1[i] + lst2[i])
    return updated_list

def find_min_max(los):
    return min(los),max(los)
sum = summation(list1,list2)
kum = find_min_max(sum)
print(sum)
print(kum)
