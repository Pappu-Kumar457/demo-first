'''num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(f"Reversed number: {reversed_num}")

sum_squares = 0
for i in range(1,6):
    sum_squares += i**2

print("Sum of squares from 1 to 5:", sum_squares)

num=int(input("Enter a number :"))
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    for i in range(2,n):
        if n%2==0:
            return False
        return True
print(test_prime(num))

def factorial(n):
    if n==0:
        return 1
    if n<0:
        return 0
    else:
        return n*factorial(n-1)
num=int(input("Enter a number :"))
print("Factorial of {} num :".format(num),factorial(num-1))'''


for num in range(1,30):
    if num%2!=0:
        if num%num==0:
         print()
    print(num)


    
            