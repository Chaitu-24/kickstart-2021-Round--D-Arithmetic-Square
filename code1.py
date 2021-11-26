t=int(input())
for j in range(1,t+1):
    arr=[[0,0,0],[0,0,0],[0,0,0]]
    arr[0][0],arr[0][1],arr[0][2]=map(int,input().split())
    arr[1][0],arr[1][2]=map(int,input().split())
    arr[2][0],arr[2][1],arr[2][2]=map(int,input().split())
    count=0
    if (arr[0][0]+arr[0][2])/2==arr[0][1]:
        count+=1
    if (arr[2][0]+arr[2][2])/2==arr[2][1]:
        count+=1
    if (arr[0][0]+arr[2][0])/2==arr[1][0]:
        count+=1
    if (arr[0][2]+arr[2][2])/2==arr[1][2]:
        count+=1
    mylist=list()
    mylist.append(arr[1][0]+arr[1][2])
    mylist.append(arr[0][1]+arr[2][1])
    mylist.append(arr[0][0]+arr[2][2])
    mylist.append(arr[2][0]+arr[0][2])
    s= set(mylist)
    coun = 0
    for i in s:
        if i%2==0:
            if coun < mylist.count(i):
                coun = mylist.count(i)
    print(f"Case #{j}: {count+coun}")
