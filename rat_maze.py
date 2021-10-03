class Solution:
    def isin(self,x,y,n):
        if(x>=0 and x<n and y>=0 and y<n):
            return True
        return False
    def dfs(self,x,y,m,n,visited,st,dirc):
        if self.isin(x,y,n):
            if m[x][y]==1:
                if(x==n-1 and y==n-1):
                    print("".join(st))
                elif not visited[x][y]:
                    visited[x][y]=True
                    for h in dirc.keys():
                        st.append(h)
                        self.dfs(x+dirc[h][0],y+dirc[h][1],m,n,visited,st,dirc)
                        st.pop(-1)
                    visited[x][y]=False
            
            
    def findPath(self, m, n):
        # code here
        dirc={"D":[1,0],"R":[0,1],"U":[-1,0],"L":[0,-1]}
        visited=[[False for i in range(n)]for j in range(n)]
        st=[]
        self.dfs(0,0,m,n,visited,st,dirc)
s=Solution()
m=[[1, 0, 0, 0],[1, 1, 0, 1], [1, 1, 0, 0],[0, 1, 1, 1]]
n=4
s.findPath(m,n)
