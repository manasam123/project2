result=0
num=int(input("enter a number"))
temp=num
while temp>0:
    rem=temp%10
    result=rem*rem*rem+result
    temp /=10
if result==num:
    print(num, "is armstrong number")
else:
    print(num,"is not a armstrong number")

