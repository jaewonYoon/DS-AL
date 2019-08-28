from sys import stdin
def sol():
    nums = []
    nums = list(stdin.readline()[:-1]) 
    nums.sort(reverse=True)
    comNums = ''
    chkNums = 0
    if(int(nums[-1]) != 0):
        return -1
    else:
        for i in nums:
           chkNums += int(i) 
           comNums += i
        if(chkNums % 3 ==0):
            return comNums
    return -1
if __name__ =="__main__":
    print(sol())
