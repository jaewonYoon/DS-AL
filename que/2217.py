from sys import stdin 
def sol():
    num = int(stdin.readline()[:-1])
    ropes = [] 
    for i in range(num):
        ropes.append(int(stdin.readline()[:-1]))
    ropes.sort(reverse=True)
    weight = ropes[0]
    for i in range(1,len(ropes)):
        if(ropes[i]*(i+1) > weight):
            weight = ropes[i] * (i+1)
    print(weight)
if __name__ == "__main__":
    sol()