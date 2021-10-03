import sys

class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def isin(x,y,m,n):

    if (x >=0 and x <= m-1 and y >= 0 and y <= n-1):
        return True
    return False

def islands(mat,m,n):
    visited=[[False for i in range(n)] for j in range(m)]
    dx=[1,0,1,-1,0,-1,-1,1]
    dy=[0,1,1,0,-1,-1,1,-1]
    k=0
    for i in range(m):

        for j in range(n):

            if mat[i][j]==0 or visited[i][j]==True:
                visited[i][j]==True
                continue

            elif mat[i][j]==1 and visited[i][j]==False:
                k+=1
                queue=[]
                queue.append(cell(i,j))
                visited[i][j]=True
                
                while(len(queue)!=0):

                    t=queue.pop(0)

                    for h in range(8):
                        x=t.x+dx[h]
                        y=t.y+dy[h]
                        
                        if isin(x,y,m,n) and visited[x][y]==False and mat[x][y]==1:
                            visited[x][y]=True
                            queue.append(cell(x,y))
                    
    return k


                




mat=[[0,1],[1,0],[1,1],[1,0]]             
print(islands(mat,4,2))
