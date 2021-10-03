def isin(x,y,m,n):
    if (x >=0 and x <= m-1 and y >= 0 and y <= n-1):
        return True
    return False

class Solution:
    def maxAreaOfIsland(self, grid):
        m=len(grid)
        n=len(grid[0])
        visited=[[False for i in range(n+1)] for j in range(m+1)]
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        q=[]
        maxa=0
        for i in range(m):
            for j in range(n):
                print(i,j)
                if grid[i][j]==1 and not visited[i][j]:
                    x1=i
                    y1=j
                    a=0
                    q.append([x1,y1])
                    visited[x1][y1]=True
                    p=0
                    while(len(q)!=0):
                        t=q.pop(0)
                        a+=1
                        for j in range(4):
                            x=t[0]+dx[j]
                            y=t[1]+dy[j]
                            if isin(x,y,m,n):
                                if not visited[x][y] and grid[x][y]==1:
                                    visited[x][y]=True
                                    q.append([x,y])
                    maxa=max(maxa,a)
        return maxa
        
s=Solution()
print(s.maxAreaOfIsland([[1,0]]))
