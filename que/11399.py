from sys import stdin
def sol():
    pple = stdin.readline()
    np = pple[:-1]
    li = stdin.readline()
    li = li[:-1]
    li = list(map(int,li.split()))
    li.sort()
    sum = 0
    for i in range(len(li)):
        j = i
        for j in range(0,j+1):
            sum += li[j]
    return sum
if __name__ == "__main__":
    print(sol())