lst = []
 
for i in range(0, 5):
    ele = int(input())
    lst.append(ele)
print(lst)
total = 0
for ele in range(0, len(lst)):
    total = total + lst[ele]
 
print("Sum of all the numbers is ", total)
