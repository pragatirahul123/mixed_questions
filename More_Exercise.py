list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
new=[]
index=0
while index<len(list1):
        if list1[index] in list2:
            new.append(list1[index])
        index=index+1
        
print(new)



