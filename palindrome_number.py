#Panlindrome Number

n = int(input("Enter the number :-"))
temp = n
rev = 0
while(n>0):
    d = n%10
    rev=rev*10+d
    n=n//10

if(temp == rev):
    print("The Number is Palindrome ")
else:
    print("The Number is not Palindrome")