a.sort()
i=1
while i<len(a):
    if a[i][0]<=a[i-1][1]:
        a[i-1][1]=max(a[i-1][1],a[i][1])
        a.pop(i)
    else:
        i+1
