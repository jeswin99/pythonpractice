def solve(h,a,i):
    if h<=0 or a<=0:
        return 0
    x=y=z=0
    if i!=1:
        x=1+solve(h+3,a+2,1)
    if i!=2:
        y=1+solve(h-5,a-10,2)
    if i!=3:
        z=1+solve(h-20,a+5,3)
    return max(x,y,z)
print(solve(20,20,1))
