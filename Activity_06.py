# For taking input of 5 numbers in the list.
lst = []
 
for i in range(0, 5):
    ele = int(input())
    lst.append(ele)
print(lst)

# for printing the first three elements in the list.
print(lst[0:3])

# for inserting 0 at starting and ending of list.
lst.insert(0, 0)
lst.append(0)
print(lst)

# for reversing the list.
lst.reverse()
print(lst)
