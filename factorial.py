n=int(input("enter the number"))
factorial=1
for i in range(1,n+1):
    fact=factorial*i
    print(n,"*",i,"=",fact)
    print("factorial",factorial,"=",fact)