
class Solution:
    #@snoop
    def makeConnected(self, n, connections):
        if len(connections)>=n-1:
            visited=set()
            k=0
            for i in range(n):
                if i not in visited:
                    k+=1
                    q=[]
                    tr=[]
                    q.append(i)
                    visited.add(i)
                    while(len(q)!=0):
                        t=q.pop(0)
                        tr.append(t)
                        for x in connections:
                            if x[0]==t and x[1] not in visited:
                                visited.add(x[1])
                                q.append(x[1])
                            if x[1]==t and x[0] not in visited:
                                visited.add(x[0])
                                q.append(x[0])
                    print(tr)
            return k-1
        else:
            return -1
s=Solution()
n=4

lst=[[0,1],[0,2],[1,2]]
print(s.makeConnected(n,lst))
