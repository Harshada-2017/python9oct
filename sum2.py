# create a heterogenous list of numbers and anmes.split the list from highest number
#accept thew name and check if its palindrome
# print the sum of digits
# print the foll pattern

n=int(input("Enter a digit:"))
sum=0
for i in range(n+1):

    sum=sum+i
print("sum",sum)

if n!=0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("sum is ",sum)
