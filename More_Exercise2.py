list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
list3=list1+list2
new=[]
index=0
while i<len(list3):
        if list3[index] not in new:
            new.append(list3[index])
        index=index+1
print(new)



