# -*- coding: utf-8 -*-
import math


for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3), end = ' ')
    print(repr(x*x*x).rjust(4))
    
    
for x in range(1,11):
    print('{0:2d} {1:3d}  {2:4d}'.format(x, x*x, x*x*x))
    
'''


Do you know why it's the original number? 
Because if you are more than 5, you don't need to change

'''
    
print("3.1231323234".zfill(5))  

print("3.1231323234".zfill(50))  


print('{}website："{}！"'.format('noobcourse','www.runoob.com'),'\n')


print('site list: {0}, {1}, {other}'.format('Google', 'baidu', other = 'Taobao'),'\n')


print('the value of the constant PI is approximated to:{!r} '.format(math.pi),'\n')




''' 

The difference between adding 'f' and not 'f':
    
    Adding 'f' The four bit refers to the decimal part
   
    Without "F", four bits include integral parts
    
    is not important!
    
    
    number 0 represents the position  ps:represents math.pi,math.pi's position is 0
    
'''

print('the value of the constant PI is approximated to :{0:.4f}。'.format(math.pi),'\n')

table = {'Google':1, 'Runoob':2, 'Taobao':3}

for name, number in table.items():
    print('{0:10}  ==> {1:10d}'.format(name, number))
    
    




