from sys import stdin

def sol():
    cost = int(stdin.readline()[:-1])
    # 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
    answer = 0
    cost = 1000- cost
    coins = [500,100,50,10,5,1]
    for i in coins:
        if(cost ==0): 
            break
        while(cost-i >=0):
            answer =answer+1
            cost = cost - i
    print(answer)
if __name__ == "__main__":
    sol()