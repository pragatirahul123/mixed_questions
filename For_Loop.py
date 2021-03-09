for i in range(8):
    print(i)



###############################################################################

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w)
    #print(w, len(w))



##########################################


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
     print(i, a[i])


####################################################




for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
