index=2
user=int(input("enetr a number"))
while index<user:
    if user%index==0:
        print(user,"not prime number")
        break
    index=index+1
else:
    print(user, "prime number")

