n=int(input("enter any positive number"))
e=int(input("enter exponent"))
p=1
for i in range(1,e+1):
    p=p*n
print("the power of number is" ,n, "^" ,e, "=" ,p)
