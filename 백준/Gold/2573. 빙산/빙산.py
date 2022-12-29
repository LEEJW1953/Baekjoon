import sys
input=sys.stdin.readline
from collections import deque

def melt(a, b):
    count=0
    for i in range(4):
        nx=b+dx[i]
        ny=a+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if arr1[ny][nx]==0:
                count+=1
        else:
            continue
    arr[a][b]-=count
    if arr[a][b]<0:
        arr[a][b]=0
    return

def bfs(a, b):
    q=deque()
    q.append([b, a])
    while q:
        [x, y]=q.popleft()
        arr[y][x]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if arr[ny][nx]!=0 and vis[ny][nx]:
                    q.append([nx, ny])
                    vis[ny][nx]=False
            else:
                continue
    return

n, m = map(int, input().split())
arr=[]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
result=0
for i in range(n):
    arr.append(list(map(int, input().split())))
while True:
    count=0
    vis=[[True]*m for _ in range(n)]

    arr1=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr1[i][j]=arr[i][j]
    for i in range(n):
        for j in range(m):
            if arr1[i][j]!=0:
                melt(i, j)
    for i in range(n):
        for j in range(m):
            arr1[i][j]=arr[i][j]

    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0:
                count+=1
                bfs(i, j)
    for i in range(n):
        for j in range(m):
            arr[i][j]=arr1[i][j]
    result+=1
    if count==0:
        result=0
        break
    elif count!=1:
        break
print(result)