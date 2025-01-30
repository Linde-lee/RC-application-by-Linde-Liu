for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("CracklePop")
    elif i % 3 == 0:
        print("Crackle")
    elif i % 5 == 0: 
        print("Pop")
    else:
        print(i)

#first i checked only print(i). then only for crackle, realised that I did not due with remainder ==0 and fixed that. 