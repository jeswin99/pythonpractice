N,M,k=[int(x) for x in input().split(" ")]
arr1=[0]
arr2=[0]
for i in range(k):
    v1,v2=[int(x) for x in input().split(" ")]
    arr1.append(v1)
    arr2.append(v2)
arr1.append(N+1)
arr2.append(M+1)
arr1.sort()
arr2.sort()
a1=max([arr1[i+1]-arr1[i]-1 for i in range(len(arr1)-1)])
a2=max([arr2[i+1]-arr2[i]-1 for i in range(len(arr2)-1)])
print(a1*a2)
