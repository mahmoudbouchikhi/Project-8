"""
functions
"""
'''
def myAdd(x,y): #parametrs
    x=x+10
    y=y+10
    sum=x+y
    print('x=',x,'y=',y)
    return sum

a=2.0
b=3.5
addValue= myAdd(a,b) #arguments
#print('a=',a,'b=',b)
print('Return value', addValue)

N=[0,1,2,3,4,5,6,7,8,9]
i=0
new_N=()
for i in range(0,len(N)):
    if i%2==0:
        N.insert(0, N.pop(i))
        #new_N=N
        #N.pop(i)

print(N)
'''
N=[0,1,2,3,4,5,6,7,8,9]
#newN=[]
N.insert(0, N.pop(-1))  # shift one place
       # shift_left(lst, n-1)  # repeat
print (N)
#return MB.insert(mc())'''