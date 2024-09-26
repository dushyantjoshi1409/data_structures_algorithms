a=8
t='dumsdfsjkdfhsadu'
c=0
r=7
for i in range (1,r+1):
    for j in range(1,a+1):
        if i==1 or j==1  or i==r or j==a:
            print("*",end=" ")
        elif i==r//2+1 and j>1 and j<a:
            print(t[c],end=' ')
            c+=1
        else:
            print(" ",end=" ")
    print()