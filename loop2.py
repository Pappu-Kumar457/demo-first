'''p=float(input('Enter Percentage:'))
if(p>=40):
    if(p>=50):
        if(p>=60):
            if(p>=70):
                print('Grade A')
            else:
                print('Grade B')
    else:
                print('Grade C')
else:
                print('Grade D')'''
                

p=float(input('Enter Percentage:'))
if(p<70):
    if(p<60):
        if(p<50):
            if(p<40):
                print('Grade D')
            else:
                print('Grade C')
    else:
                print('Grade B')
else:
                print('Grade A')
                