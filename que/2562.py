from __future__ import print_function
from sys import stdin
max = 0
max_index= 0
for i in range(9):
    a =int(stdin.readline())
    if(max<= a):
        max = a
        max_index = i
print(max,max_index+1,sep='\n')
    
