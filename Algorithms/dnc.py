#Divide and Conquer

slist=[10,23,53,60,78,83,85,91,100]#정렬된 배열

#x=int(input("찾고싶은 정수:"))
#순차검색
def Linear_Search(list,x):
    for i in list:
        if i==x:
            return True
    return False
#이진검색
def Binary_Search(low,high,list,x):#Recursive Algorithm
    if(low>high):
        return "없음"
    else:
        mid=(low+high)//2
        if (x==list[mid]):
            return str(mid)+"번째에 있음"
        elif(x<list[mid]):#왼쪽으로 반띵
            return Binary_Search(low,mid-1,list,x)
        else:#오른쪽으로 반띵
            return Binary_Search(mid+1,high,list,x)
def Binary_Search2(list,x):#iterative Algorithm
    low=0
    high=len(list)-1
    loca=-1
    while(low<=high):
        mid=(low+high)//2
        if(x==list[mid]):
            loca=mid
            break
        elif(x<list[mid]):
            high=mid-1
        else:
            low=mid+1
    return loca

#print(Binary_Search(0,len(slist)-1,slist,x))
#print(Binary_Search2(slist,x))
# if Linear_Search(slist,x)==True:
#     print("in Array")
# else:
#     print("NOooo")



