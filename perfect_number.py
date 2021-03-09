num = int(input("Enter any number: "))
sum1 = 0
index=1
while index<(num):
    if(num % index == 0):
        sum1 = sum1 + index
    index=index+1
        
if (sum1 == num):
        print("yes, Perfect number!")
else:
        print("no, Perfect number!")
