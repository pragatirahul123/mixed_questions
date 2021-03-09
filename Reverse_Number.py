list=1234
rev=0
while list>0:
	rem=list%10
	rev=rev*10+rem
	list=list//10
print(rev)
