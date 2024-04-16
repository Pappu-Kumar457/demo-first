#QS1
'''
array=[4,6,8,2,9,4,55,78,23,55]
array.sort()
print(array) 
print(type(array))

#QS:2
def remove_non_int(list1):
    list2 = [x for x in list1 if isinstance(x, int)]
    return list2
list1=[1,3,4,6,8,9,4,["ant","flower","fruits","cars"]]

list2=remove_non_int(list1)
print(list2)

# OR
list1=['2','4','5','6.402','8.3025','6.015','9','8.4','ant','fruit','cars']

list2=[a for a in list1 if a.isnumeric()]
list3=[a for a in list1 if a.isfloat()]
list4=[a for a in list1 if a.isalpha()] # for string
print(list2)
print(list3)
print(list4)

#QS 3

list1=[1,2,3,4,5,6,9]
avg=sum(list1)/len(list1)
print(avg)

#QS 4

def prime_num(n):
    primes=[]
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j == 0:
               break
        else :
            primes.append(i)
    return primes
num1=prime_num(100)
print(num1)


#QS 5

fabc2=0
fabc1=1
print(fabc2)
print(fabc1)
print()
for i in range(10):
    new_fabc=fabc2+fabc1
    print(new_fabc)
    fabc2=fabc1
    fabc1=new_fabc'''

#QS

def factorial(n):
   
    if n<0:
        return 0
    else:
        return n*(n-1)
    
num=factorial(15)
print(num)



