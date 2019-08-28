from sys import stdin

def sol():
    arr = list(map(int,stdin.readline()[:-1].split()))
    n = arr[0]
    m = arr[1]
    k = arr[2]
    if(n < 2 or m < 1):
        return 0 
    # woman has lack of number 
    elif(n <= m*2):
        answer = n//2
        m = m - n//2
        k -= m
        while(k>0 and answer >0):
            k -= 3
            m -= 1
            answer -= 1
        return answer
    #man has lack of number
    elif (n > m*2):
        answer =  m 
        n -= m*2
        k -= n 
        while(k > 0 and answer > 0):
            k -= 3 
            m -=1
            answer -= 1
        return answer
    
if __name__ =="__main__":
    print(sol())
        
            
        