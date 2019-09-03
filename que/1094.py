
from sys import stdin
def sol():
    stk = int(stdin.readline()[:-1])
    answer = merge(64,stk)
    return answer 
def merge(n,x):
    if(n == x ):
        return 1
    elif(n//2 <x):
        return (1 + merge(n//2, x-n//2))
    else:
        return  merge(n//2, x)
if __name__ == "__main__":
    print(sol())