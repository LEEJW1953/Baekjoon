import sys
input=sys.stdin.readline

n=int(input())
arr=[]
count=0
for i in range(n):
    arr.append(int(input()))
for i in range(n-1, 0, -1):
    if arr[i-1]>=arr[i]:
        count+=(arr[i-1]-arr[i]+1)
        arr[i-1]=arr[i]-1
print(count)