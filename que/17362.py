from sys import stdin
def sol():
    num = int(stdin.readline()[:-1])
    if( num % 8 == 1):
        return 1
    elif(num % 8 == 2 or num % 8 == 0):
        return 2
    elif(num % 8 == 3 or num % 8 == 7):
        return 3
    elif(num % 8 == 4 or num % 8 == 6):
        return 4
    else:
        return 5
if __name__ == "__main__": 
    print(sol())

